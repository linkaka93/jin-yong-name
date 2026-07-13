# Install `jin-yong-name`

Install the complete Agent Skill without opening an interactive Agent-selection menu.

Run:

```bash
curl -fsSL https://raw.githubusercontent.com/linkaka93/jin-yong-name/main/install.sh | sh
```

The installer detects WorkBuddy, Codex, Claude Code, Cursor, Gemini CLI and GitHub Copilot. If it cannot identify the current Agent, it installs to the shared `~/.agents/skills/` directory.

For WorkBuddy specifically:

```bash
curl -fsSL https://raw.githubusercontent.com/linkaka93/jin-yong-name/main/install.sh | sh -s -- --agent workbuddy
```

For another Agent with a custom skills directory:

```bash
curl -fsSL https://raw.githubusercontent.com/linkaka93/jin-yong-name/main/install.sh | sh -s -- --target /path/to/agent/skills
```

The installation is successful only when the complete directory is present, including `SKILL.md`, `references/`, `scripts/`, `evals/` and `agents/`.
