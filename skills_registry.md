# skills.yaml

Save this file as `.claude/skills.yaml`.

```yaml
version: "1.0.0"

shared_skills:

  strategic-planning:
    category: executive
    used_by:
      - dario-amodei
      - elon-musk
      - sam-altman

  software-architecture:
    category: engineering
    used_by:
      - jeff-dean
      - sanjay-ghemawat
      - leslie-lamport

  api-design:
    category: backend
    used_by:
      - patrick-collison

  prompt-engineering:
    category: ai
    used_by:
      - amanda-askell
      - john-schulman

  llm-evaluation:
    category: ai
    used_by:
      - percy-liang
      - dan-hendrycks

  threat-modeling:
    category: security
    used_by:
      - adam-shostack

  cryptography:
    category: security
    used_by:
      - dan-boneh

  incident-response:
    category: security
    used_by:
      - kevin-mandia

  automated-testing:
    category: qa
    used_by:
      - angie-jones
      - michael-feathers

defaults:
  reuse_shared_skills: true
  duplicate_skill_definitions: false
  inheritance: enabled
```
