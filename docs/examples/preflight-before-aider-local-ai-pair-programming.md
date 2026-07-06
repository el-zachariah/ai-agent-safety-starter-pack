# Preflight before Aider local AI pair-programming

Marker: `AIDER_LOCAL_AI_PAIR_PROGRAMMING_PROOF`

Public target evidence checked during this deadline pulse:

- Target repo: [`Aider-AI/aider`](https://github.com/Aider-AI/aider)
- Stars observed: `47094`
- Last updated: `2026-07-06T06:17:47Z`
- Public description: aider is AI pair programming in your terminal

## Why this proof exists

Aider-style terminal pair-programming happens inside a real Git checkout, so a buyer needs a quick receipt before AI-suggested edits, tests, package scripts, or secret-adjacent files enter the run.

This page is not a claim that the upstream project uses this pack. It is a buyer-specific example showing how an Aider local AI pair-programming teams maintainer can make the $7 pack feel concrete before checkout.

## 90-second free preflight

1. Clone or open the repo where the Aider run will happen.
2. Run the free scanner from this public repo before accepting broad edits or command execution:

```bash
python3 scripts/agent_preflight_lite.py --path . --format markdown --output agent-preflight.md
```

3. Attach `agent-preflight.md` to the task, PR, issue, or local run notes.
4. Use the result as the go/no-go gate before the assistant touches install scripts, package manager hooks, `.env*`, CI workflows, MCP/tool configuration, or generated shell commands.

## Buy / skip trigger

- **Green:** keep using the free scanner and skip the paid pack for now.
- **Yellow / Red:** buy the $7 **AI Agent Safety Starter Pack** at https://payhip.com/b/1nmxV and use the full checklist, hook template, prompt, and preflight receipt before the next agent run.

`YELLOW_RED_BUY_TRIGGER_AIDER`

## Aider run-ticket receipt template

Copy this into the run ticket before the Aider session starts:

```markdown
### Agent preflight before Aider run
- Target repo/path:
- Requested Aider task:
- Free scanner receipt attached: yes/no
- Decision level: Green / Yellow / Red
- Risk buckets: secrets / package scripts / CI / MCP tools / deploy config / generated shell
- If Yellow/Red, paid pack checklist applied: yes/no
- Human owner approving the run:
```

## What the paid pack adds for this segment

The public scanner proves the risk signal. The paid pack adds the repeatable operating layer: command-hook checklist, copy/paste task prompt, reviewer receipt template, and a compact preflight workflow that helps a real buyer decide whether the local AI pair-programming session is safe enough to start.

Primary checkout: https://payhip.com/b/1nmxV
