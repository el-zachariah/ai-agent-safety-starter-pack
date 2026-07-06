# Preflight before Vercel AI SDK tool-calling agents

**Vercel AI SDK agent preflight proof.** Use this when a TypeScript/Next.js team is about to let an AI SDK agent, tool call, MCP connector, server action, route handler, or eval script operate against a real repository or deployment environment.

Target evidence checked during this pulse: [`vercel/ai`](https://github.com/vercel/ai) was public on GitHub with 25365 stars and updated at `2026-07-06T02:49:38Z`. Description observed: "The AI Toolkit for TypeScript. From the creators of Next.js, the AI SDK is a free open-source library for building AI-powered applications and agents".

## Why this buyer should care

Vercel AI SDK projects often combine model providers, streaming route handlers, server actions, tool definitions, package scripts, `.env` values, and preview/deploy settings. A small agent mistake can move from local code into a live Next.js or Vercel workflow quickly, so the buyer needs a short receipt before the agent gets repo, shell, or credential-adjacent scope.

## Five-minute free preflight

1. Run the free scanner before granting the AI SDK workflow package-script, MCP/tool, or deployment scope:

   ```bash
   python3 agent_preflight_lite.py --repo /path/to/nextjs-ai-sdk-app --output-md agent-preflight-vercel-ai-sdk.md --output-json agent-preflight-vercel-ai-sdk.json
   ```

2. In the receipt, look for:
   - `.env`, `.env.local`, Vercel/project config, and provider-key placeholders;
   - `package.json` scripts that can build, deploy, seed data, or run local servers;
   - AI SDK tool functions, server actions, route handlers, eval scripts, MCP/API connectors, or webhook code;
   - repo instructions such as `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, `.cursor/rules/*`, or GitHub Copilot instructions;
   - generated **Green / Yellow / Red** decision before the agent starts.

3. Paste the Markdown receipt into the task issue, PR, or deployment approval note before the AI SDK agent receives broad repo or shell scope.

## When to buy the $7 pack

Buy the paid pack if the receipt is **Yellow/Red**, if the AI SDK workflow can run package scripts or deployment helpers, or if provider keys, MCP/API tools, route handlers, server actions, or preview/deploy settings are in scope: https://payhip.com/b/1nmxV

Skip it for now if the receipt is **Green**, the app has no credential-adjacent files or tool-running paths, and the free scan plus normal code review is enough.

## Copy-paste approval note

> I ran `agent-preflight-vercel-ai-sdk` before granting AI SDK agent/tool scope. Current decision: `<Green|Yellow|Red>`. If Yellow/Red, I will reduce tool/deploy scope or use the paid starter pack checklist before enabling package scripts, route-handler changes, MCP/API connectors, or provider-key-adjacent work.

Related free repo assets: [`/agent-preflight`](../../commands/agent-preflight.md), [review-comment template](../preflight-review-comment-template.md), and [trust/support notes](../trust-and-support.md).
