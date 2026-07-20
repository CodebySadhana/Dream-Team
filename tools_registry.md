# tools.yaml

Save this file as `.claude/tools.yaml`.

```yaml
version: "1.0.0"

tools:
  Read:
    description: Read files
    approval: false

  Edit:
    description: Modify files
    approval: false

  Grep:
    description: Search repository
    approval: false

  Glob:
    description: File discovery
    approval: false

  Bash:
    description: Execute shell commands
    approval: true

  Task:
    description: Delegate work to subagents
    approval: false

agent_permissions:

  dario-amodei:
    allow: [Read, Grep, Glob, Task]
    deny: [Edit, Bash]

  mira-murati:
    allow: [Read, Grep, Glob, Task]
    deny: []

  jeff-dean:
    allow: [Read, Edit, Grep, Glob, Bash]
    deny: []

  parisa-tabriz:
    allow: [Read, Grep, Task]
    deny: [Edit]

defaults:
  approval_mode: on-request
  least_privilege: true
```
