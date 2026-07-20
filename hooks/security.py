#!/usr/bin/env python3
"""
security-check.py

Loop-Engineered Dream Team
Claude Code Security Verification Hook

Purpose:
- Runs before deployment and release approval
- Detects common security risks
- Produces a standardized security report
- Blocks deployment on critical findings

Owner:
Parisa Tabriz Agent

Review Agents:
Adam Shostack Agent
Dan Boneh Agent
Anton Chuvakin Agent
Kevin Mandia Agent
Mark Russinovich Agent
"""

from pathlib import Path
import re
import json
import sys
from datetime import datetime


# ==========================================
# Configuration
# ==========================================

CRITICAL_PATTERNS = [
    r"password\s*=",
    r"secret\s*=",
    r"api_key\s*=",
    r"private_key",
    r"AWS_SECRET_ACCESS_KEY",
    r"BEGIN RSA PRIVATE KEY",
    r"BEGIN PRIVATE KEY",
]

HIGH_PATTERNS = [
    r"eval\(",
    r"exec\(",
    r"subprocess\.Popen",
    r"os\.system",
    r"shell=True",
]

MEDIUM_PATTERNS = [
    r"TODO.*security",
    r"FIXME.*security",
    r"bypass_auth",
]

ALLOWED_EXTENSIONS = {
    ".py",
    ".js",
    ".ts",
    ".tsx",
    ".jsx",
    ".java",
    ".go",
    ".rs",
    ".json",
    ".yaml",
    ".yml",
    ".md",
}


# ==========================================
# Models
# ==========================================

class Finding:
    def __init__(self, severity, file_path, line_no, message):
        self.severity = severity
        self.file_path = file_path
        self.line_no = line_no
        self.message = message

    def to_dict(self):
        return {
            "severity": self.severity,
            "file": self.file_path,
            "line": self.line_no,
            "message": self.message,
        }


# ==========================================
# Scanner
# ==========================================

def scan_file(path):
    findings = []

    try:
        content = path.read_text(
            encoding="utf-8",
            errors="ignore"
        )
    except Exception:
        return findings

    lines = content.splitlines()

    for line_no, line in enumerate(lines, start=1):

        for pattern in CRITICAL_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                findings.append(
                    Finding(
                        "CRITICAL",
                        str(path),
                        line_no,
                        f"Potential secret detected ({pattern})"
                    )
                )

        for pattern in HIGH_PATTERNS:
            if re.search(pattern, line):
                findings.append(
                    Finding(
                        "HIGH",
                        str(path),
                        line_no,
                        f"Potential unsafe execution ({pattern})"
                    )
                )

        for pattern in MEDIUM_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                findings.append(
                    Finding(
                        "MEDIUM",
                        str(path),
                        line_no,
                        f"Security review required ({pattern})"
                    )
                )

    return findings


def scan_repository(root):
    findings = []

    for path in Path(root).rglob("*"):

        if not path.is_file():
            continue

        if path.suffix.lower() not in ALLOWED_EXTENSIONS:
            continue

        findings.extend(scan_file(path))

    return findings


# ==========================================
# Reporting
# ==========================================

def create_report(findings):

    summary = {
        "CRITICAL": 0,
        "HIGH": 0,
        "MEDIUM": 0,
    }

    for f in findings:
        summary[f.severity] += 1

    report = {
        "timestamp": datetime.utcnow().isoformat(),
        "summary": summary,
        "findings": [f.to_dict() for f in findings]
    }

    return report


def save_report(report):

    reports_dir = Path(".claude/security")
    reports_dir.mkdir(parents=True, exist_ok=True)

    report_file = reports_dir / "latest-security-report.json"

    with open(report_file, "w") as f:
        json.dump(report, f, indent=2)

    return report_file


# ==========================================
# Decision Engine
# ==========================================

def deployment_allowed(report):

    if report["summary"]["CRITICAL"] > 0:
        return False

    return True


# ==========================================
# Main
# ==========================================

def main():

    root = Path.cwd()

    print("\n[Security Hook] Starting security verification...\n")

    findings = scan_repository(root)

    report = create_report(findings)

    report_file = save_report(report)

    print(f"Security Report: {report_file}")

    print(
        f"CRITICAL={report['summary']['CRITICAL']} "
        f"HIGH={report['summary']['HIGH']} "
        f"MEDIUM={report['summary']['MEDIUM']}"
    )

    if deployment_allowed(report):
        print("\nPASS: Security verification successful")
        sys.exit(0)

    print("\nFAIL: Critical security issues detected")
    sys.exit(1)


if __name__ == "__main__":
    main()