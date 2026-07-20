# Planning Loop

**Save as:** `.claude/loops/planning-loop.md`

## Purpose

The Planning Loop is the standard reasoning cycle used by every
supervisor and specialist agent before execution. It ensures work is
understood, delegated, verified, and continuously improved.

## Loop Definition

``` text
INPUT
  ↓
Understand Request
  ↓
Gather Context
  ↓
Analyze Constraints
  ↓
Identify Dependencies
  ↓
Create Task Plan
  ↓
Assign Responsible Agent(s)
  ↓
Self Review
  ↓
Supervisor Review
  ↓
Approve
  ↓
Execute
  ↓
Collect Results
  ↓
Verify
  ↓
Store Memory
  ↓
END
```

## Rules

1.  Never skip context gathering.
2.  Break large objectives into atomic tasks.
3.  Assign a single owner for every task.
4.  Verify every deliverable before completion.
5.  Escalate blockers immediately.
6.  Update organizational memory after completion.

## Inputs

-   User objective
-   Organizational goals
-   Existing memory
-   Knowledge base
-   Project constraints

## Outputs

-   Approved execution plan
-   Task assignments
-   Risk register
-   Success criteria

## Success Criteria

-   Objective clearly defined
-   Tasks assigned
-   Risks documented
-   Verification completed
-   Memory updated

## Failure Recovery

If verification fails:

1.  Identify root cause.
2.  Re-plan affected tasks.
3.  Reassign if necessary.
4.  Repeat the loop until verification succeeds.
