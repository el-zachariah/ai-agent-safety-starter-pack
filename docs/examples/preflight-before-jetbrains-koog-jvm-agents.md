# Preflight before JetBrains Koog JVM/Kotlin agent workflows

Named customer segment: teams building JVM, Kotlin, Android/iOS, or backend AI agents with JetBrains Koog before granting tool calls, package scripts, Gradle/Maven tasks, API connectors, deployment config, or secret-adjacent environment values to an agent run in a real repository.

Public evidence checked in this pulse: [`JetBrains/koog`](https://github.com/JetBrains/koog) is live, not archived, had 4,423 GitHub stars when checked, was updated `2026-07-06T11:55:27Z`, and describes itself as: "Koog is a JVM (Java and Kotlin) framework for building predictable, fault-tolerant and enterprise-ready AI agents across all platforms – from backend services to Android and iOS, JVM, and even in-browser environments. Koog is based on our AI products expertise and provides proven solutions for complex LLM and AI problems".

This is not an affiliation or endorsement. It is a concrete first-buyer proof for developers who already use Kotlin/JVM agent workflows but need a fast local receipt before the workflow touches a real checkout.

## 60-second preflight receipt

Run the free scanner in the repository the Koog workflow will read or mutate:

```bash
python3 agent_preflight_lite.py /path/to/koog-agent-repo --markdown > jetbrains-koog-jvm-agent-preflight.md
python3 agent_preflight_lite.py /path/to/koog-agent-repo --json > jetbrains-koog-jvm-agent-preflight.json
```

Attach the Markdown receipt to the task, issue, PR, or run notes before widening agent scope.

## What the receipt should name

- Build and runtime files such as `build.gradle.kts`, `settings.gradle.kts`, `pom.xml`, `gradle.properties`, lockfiles, Dockerfiles, and CI workflows.
- Agent/tool configuration that can reach local files, shell commands, HTTP/API tools, MCP servers, browser automation, model keys, or secret-adjacent `.env` paths.
- Generated-code boundaries: which modules the agent may edit, which Gradle/Maven/test commands it may run, and which connectors stay read-only.
- Android/iOS/backend deploy paths, publishing tasks, migrations, or package-release commands that must remain human-approved.

## Copy-paste run-ticket note

```text
JetBrains Koog JVM/Kotlin agent preflight receipt
Repo/task: <link>
Agent/tool scope requested: <read-only / write / shell / API connector / deploy-adjacent>
Preflight result: <Green / Yellow / Red>
Risk buckets named: <Gradle/Maven scripts, CI workflows, env/secrets, agent config, generated edits>
Allowed commands: <exact commands>
Must ask before: <publish, deploy, migration, destructive shell, credential/API access, external side effects>
Decision: <run free / pause and buy starter pack / do not run>
Marker: JETBRAINS_KOOG_JVM_AGENT_PROOF
```

## Buy / skip trigger

- **Green:** keep the free receipt and run with narrow, least-privilege tool scope. Do not buy yet.
- **Yellow:** buy the `$7` AI Agent Safety Starter Pack at <https://payhip.com/b/1nmxV> if the team wants the reusable handoff template, destructive-command hook, and reviewer prompts before widening agent scope.
- **Red:** stop the run and use the paid pack's repeatable preflight workflow before allowing shell, write, publish/deploy, or credential-backed tools.

The paid bundle is positioned here only for teams that saw real Yellow/Red repo risk and want a ready-made local workflow instead of rebuilding the same receipt, hook, and review checklist for each Koog-style agent run.
