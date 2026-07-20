# **Loop-Engineered Dream Team**

## **Volume II**

### **Specialist Agent Architecture**

**Subtitle**

**Designing the Specialist Layer for Claude Code & Codex**

---

# **Table of Contents**

1\. Specialist Agent Architecture  
2\. Backend Engineering Organization  
3\. AI Engineering Organization  
4\. Security Organization  
5\. QA Organization  
6\. Design Organization  
7\. Marketing Organization  
8\. Finance Organization  
9\. Operations Organization  
10\. Legal Organization  
11\. Agent Collaboration Matrix  
12\. Escalation Rules  
13\. Tool Permissions  
14\. Loop Contracts  
15\. Codex Execution Layer  
---

# **Chapter 1**

## **Specialist Agent Philosophy**

Supervisor agents never solve every problem themselves.

Instead they

Receive Goal

↓

Plan

↓

Delegate

↓

Review

↓

Approve

Specialists

Receive Task

↓

Solve

↓

Verify

↓

Return Result

Each specialist should own **one primary capability**, have a clearly defined interface (inputs/outputs), and avoid overlapping responsibilities where possible. This makes delegation predictable and simplifies verification.

---

# **Chapter 2**

# **Backend Engineering Organization**

## **Supervisor**

### **Sanjay Ghemawat Agent**

Mission

Own all backend engineering.

Responsibilities

* architecture implementation  
* APIs  
* distributed systems  
* storage  
* reliability  
* rollback

Loop

Architecture

↓

Implementation

↓

Review

↓

Testing

↓

Optimization  
---

## **Patrick Collison Agent**

### **Primary Skill**

API Development

Secondary Skills

* SDK Design  
* Developer Experience  
* Documentation  
* Versioning  
* Platform APIs

Loop

Requirements

↓

API Design

↓

SDK

↓

Documentation

↓

Review

Outputs

* API Spec  
* SDK Plan  
* Integration Guide

---

## **Martin Kleppmann Agent**

Primary Skill

State Management

Skills

* Event Sourcing  
* CQRS  
* Local-first  
* Data Modeling  
* Consistency Models

Outputs

* State Model  
* Event Schema  
* Consistency Analysis

---

## **Michael Stonebraker Agent**

Primary Skill

Database Design

Skills

* SQL  
* OLTP  
* OLAP  
* Query Planning  
* Storage

Outputs

* Database Architecture  
* Schema  
* Optimization Plan

---

## **Leslie Lamport Agent**

Primary Skill

Distributed Systems

Skills

* Consensus  
* Paxos  
* Formal Specs  
* TLA+  
* Fault Tolerance

Outputs

* Formal Specification  
* Distributed Protocol  
* Safety Proof

---

## **Mitchell Hashimoto Agent**

Primary Skill

Rollback Engineering

Skills

* Infrastructure as Code  
* Terraform  
* State Recovery  
* Automation  
* GitOps

Outputs

* Rollback Strategy  
* Recovery Workflow  
* IaC Blueprint

---

# **Backend Internal Loop**

API

↓

Database

↓

Distributed System

↓

Rollback

↓

Review  
---

# **Chapter 3**

# **AI Engineering Organization**

Supervisor

## **Andrej Karpathy Agent**

Mission

Build intelligent systems.

Responsibilities

* LLMs  
* AI pipelines  
* inference  
* prompting  
* evaluation

---

## **John Schulman Agent**

Primary Skill

Tool Calling

Skills

* RLHF  
* PPO  
* Function Calling  
* Agents  
* Planning

Outputs

* Tool Graph  
* Tool Strategy

---

## **Amanda Askell Agent**

Primary Skill

Prompt Engineering

Skills

* Prompt Design  
* Safety  
* Model Behavior  
* Character Design  
* Constitutional AI

Outputs

* System Prompt  
* Persona  
* Safety Rules

---

## **Percy Liang Agent**

Primary Skill

Evaluation

Skills

* Benchmarks  
* Metrics  
* Evaluation  
* Safety  
* Robustness

Outputs

* Evaluation Report  
* Benchmark Results

---

## **Noam Shazeer Agent**

Primary Skill

Routing

Skills

* Mixture of Experts  
* Transformer Routing  
* Token Routing  
* Architecture

Outputs

* Routing Plan  
* Architecture

---

## **Patty McCord Agent**

Primary Skill

Compensation

Skills

* Hiring  
* Talent  
* Compensation  
* Culture

Outputs

* Compensation Plan  
* Hiring Policy

---

# **AI Loop**

Prompt

↓

Planning

↓

Tools

↓

Inference

↓

Evaluation

↓

Optimization  
---

# **Chapter 4**

# **Security Organization**

Supervisor

## **Parisa Tabriz Agent**

Mission

Secure everything.

---

### **Adam Shostack Agent**

Threat Modeling

Skills

* STRIDE  
* DFD  
* Attack Trees

---

### **Dan Boneh Agent**

Access Control

Skills

* Cryptography  
* PKI  
* Identity  
* Encryption

---

### **Anton Chuvakin Agent**

Audit Logging

Skills

* SIEM  
* Logging  
* Detection  
* Telemetry

---

### **Kevin Mandia Agent**

Incident Response

Skills

* IR  
* Forensics  
* Containment  
* Recovery

---

### **Mark Russinovich Agent**

Safe Systems

Skills

* Kernel  
* Memory Safety  
* Cloud Security  
* Diagnostics

---

# **Security Loop**

Threat Model

↓

Defense

↓

Logging

↓

Monitoring

↓

Response  
---

# **Chapter 5**

# **QA Organization**

Supervisor

## **James Whittaker Agent**

Mission

Assure quality.

---

### **Angie Jones Agent**

Automation

Skills

* Selenium  
* Playwright  
* Automation  
* CI/CD

---

### **Michael Feathers Agent**

Regression Testing

Skills

* Legacy Code  
* Characterization Tests  
* Refactoring

---

### **Nicholas Carlini Agent**

Adversarial Testing

Skills

* Red Teaming  
* Prompt Injection  
* Model Extraction  
* Robustness

---

### **Dan Hendrycks Agent**

Benchmark Creation

Skills

* MMLU  
* Safety Benchmarks  
* Capability Evaluation

---

# **QA Loop**

Unit Test

↓

Integration Test

↓

Regression

↓

Adversarial Test

↓

Benchmark  
---

# **Chapter 6**

# **Specialist Collaboration Matrix**

| Department | Primary Collaborates With |
| ----- | ----- |
| Backend | Product, AI, QA |
| AI | Backend, Security, QA |
| Security | Backend, AI |
| QA | Every Department |
| Product | Design, Marketing |
| Operations | Engineering, Finance |

---

# **Chapter 7**

# **Escalation Rules**

Level 1

Specialist

↓

Level 2

Supervisor

↓

Level 3

CEO Agent

↓

Human

Escalation triggers include:

* conflicting technical recommendations  
* unresolved architectural trade-offs  
* security-critical findings  
* failed verification after retry budget  
* decisions exceeding delegated authority

---

# **Chapter 8**

# **Tool Permissions**

Each specialist receives only the tools required for its domain.

Example:

Patrick Collison

✓ API Generator

✓ Documentation

✓ SDK Builder

✗ Security Keys

✗ Deployment  
Kevin Mandia

✓ Incident Logs

✓ Forensics

✓ Security Dashboard

✗ Product Roadmap

This least-privilege approach reduces unnecessary context sharing and aligns with the principle of isolating specialized agent contexts.

---

# **Chapter 9**

# **Codex Execution Layer**

User

↓

CEO Agent

↓

Supervisor

↓

Specialist

↓

Codex

↓

Verification

↓

QA

↓

Supervisor Approval

↓

CEO Approval

↓

User  
