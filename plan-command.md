# /plan Command

**Save as:** `.claude/commands/plan.md`

## Purpose

The `/plan` command is the standard entry point for planning across the
Dream Team AI Operating System. It converts a user objective into a
verified execution plan and routes work to the correct supervisor and
specialist agents.

## Invocation

``` text
/plan <objective>
```

Example:

``` text
/plan Build a multi-agent RAG platform with authentication and monitoring.
```

## Execution Pipeline

``` text
User Request
      ↓
CEO Agent
      ↓
Determine Department(s)
      ↓
Assign Supervisor(s)
      ↓
Run Planning Loop
      ↓
Break Down Tasks
      ↓
Assign Specialist Agents
      ↓
Review Plan
      ↓
Approve
      ↓
Ready for Execution
```

## Required Output

Every execution plan must include:

-   Objective
-   Scope
-   Assumptions
-   Constraints
-   Task Breakdown
-   Assigned Agents
-   Dependencies
-   Risks
-   Timeline
-   Success Metrics

## Rules

1.  Clarify ambiguous objectives before planning.
2.  Assign one primary owner for each task.
3.  Record dependencies explicitly.
4.  Route cross-functional work through the appropriate supervisors.
5.  Do not begin implementation until the plan is approved.

## Failure Handling

If planning cannot complete:

-   Identify blockers.
-   Request missing information.
-   Escalate unresolved conflicts.
-   Retry after updates.

## Success Criteria

A successful `/plan` command produces:

-   A complete execution roadmap.
-   Verified task ownership.
-   Documented risks.
-   Clear acceptance criteria.
