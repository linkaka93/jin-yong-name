#!/bin/sh
set -eu

REPO="linkaka93/jin-yong-name"
BRANCH="main"
SKILL_NAME="jin-yong-name"
HOME_DIR="${HOME:?HOME is not set}"

usage() {
  printf '%s\n' "Usage: install.sh [--agent workbuddy|codex|claude-code|cursor|gemini|copilot] [--target DIR]"
}

agent="auto"
target_root=""

while [ "$#" -gt 0 ]; do
  case "$1" in
    --agent)
      [ "$#" -ge 2 ] || { usage; exit 2; }
      agent="$2"
      shift 2
      ;;
    --target)
      [ "$#" -ge 2 ] || { usage; exit 2; }
      target_root="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      printf 'Unknown argument: %s\n' "$1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

if [ -z "$target_root" ]; then
  if [ "$agent" = "auto" ]; then
    if [ -n "${WORKBUDDY_HOME:-}" ] || [ -d "$HOME_DIR/.workbuddy" ]; then
      agent="workbuddy"
    elif [ -n "${CODEX_HOME:-}" ] || [ -d "$HOME_DIR/.codex" ]; then
      agent="codex"
    elif [ -n "${CLAUDE_CONFIG_DIR:-}" ] || [ -d "$HOME_DIR/.claude" ]; then
      agent="claude-code"
    elif [ -d "$HOME_DIR/.cursor" ]; then
      agent="cursor"
    elif [ -d "$HOME_DIR/.gemini" ]; then
      agent="gemini"
    elif [ -d "$HOME_DIR/.copilot" ]; then
      agent="copilot"
    else
      agent="shared"
    fi
  fi

  case "$agent" in
    workbuddy)
      target_root="${WORKBUDDY_HOME:-$HOME_DIR/.workbuddy}/skills"
      ;;
    codex)
      target_root="${CODEX_HOME:-$HOME_DIR/.codex}/skills"
      ;;
    claude|claude-code)
      target_root="${CLAUDE_CONFIG_DIR:-$HOME_DIR/.claude}/skills"
      ;;
    cursor)
      target_root="$HOME_DIR/.cursor/skills"
      ;;
    gemini|gemini-cli)
      target_root="$HOME_DIR/.gemini/skills"
      ;;
    copilot|github-copilot)
      target_root="$HOME_DIR/.copilot/skills"
      ;;
    shared|cline|opencode|windsurf|roo)
      target_root="$HOME_DIR/.agents/skills"
      ;;
    *)
      printf 'Unsupported agent name: %s\n' "$agent" >&2
      printf '%s\n' 'Use --target /your/agent/skills for another Agent.' >&2
      exit 2
      ;;
  esac
fi

for command_name in curl tar mktemp; do
  command -v "$command_name" >/dev/null 2>&1 || {
    printf 'Required command not found: %s\n' "$command_name" >&2
    exit 1
  }
done

tmp_dir=$(mktemp -d "${TMPDIR:-/tmp}/jin-yong-name.XXXXXX")
cleanup() {
  rm -rf "$tmp_dir"
}
trap cleanup EXIT HUP INT TERM

archive="$tmp_dir/repo.tar.gz"
source_dir="$tmp_dir/jin-yong-name-$BRANCH/skills/$SKILL_NAME"
archive_url="https://github.com/$REPO/archive/refs/heads/$BRANCH.tar.gz"

printf '%s\n' "Downloading $REPO..."
curl -fsSL "$archive_url" -o "$archive"
tar -xzf "$archive" -C "$tmp_dir"

[ -f "$source_dir/SKILL.md" ] || {
  printf '%s\n' 'Downloaded package is missing SKILL.md.' >&2
  exit 1
}

mkdir -p "$target_root"
target_dir="$target_root/$SKILL_NAME"
rm -rf "$target_dir"
cp -R "$source_dir" "$target_dir"

[ -f "$target_dir/references/03_好名字评判标准.md" ] || {
  printf '%s\n' 'Installation is incomplete: references are missing.' >&2
  exit 1
}
[ -f "$target_dir/scripts/name_quality_check.py" ] || {
  printf '%s\n' 'Installation is incomplete: scripts are missing.' >&2
  exit 1
}

if command -v python3 >/dev/null 2>&1; then
  python3 "$target_dir/evals/validate_skill_contract.py"
fi

printf '\nInstalled %s for %s:\n%s\n' "$SKILL_NAME" "$agent" "$target_dir"
printf '%s\n' 'Restart the Agent or open a new session if the skill is not detected immediately.'
