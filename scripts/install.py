#!/usr/bin/env python3
"""Install a skill from this repo into ~/.agents/skills, then symlink it into each selected
agent's skills dir so they all share one install.

    ~/.agents/skills/<skill>              # the install (a copy of the skill)
    ~/.<agent>/skills/<skill>  ->  hub    # a symlink, one per selected agent

Run from anywhere — paths resolve against the repo root (this script's parent directory).

Usage:
    python3 scripts/install.py                              # install skills/to-ssdl; agents: claude, codex
    python3 scripts/install.py --agents claude,codex,cursor
    python3 scripts/install.py --skill skills/<other>       # install a different skill in this repo
    python3 scripts/install.py --link                       # hub is a symlink to the repo skill (dev: edits propagate)
    python3 scripts/install.py --uninstall
    python3 scripts/install.py --dry-run
"""
from __future__ import annotations
import argparse
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent    # the repo root (this script lives in scripts/)
DEFAULT_SKILL = "skills/to-ssdl"
DEFAULT_AGENTS = ["claude", "codex"]


def rm(p: Path) -> None:
    """Remove a path whether it's a symlink, file, or directory."""
    if p.is_symlink() or p.is_file():
        p.unlink()
    elif p.is_dir():
        shutil.rmtree(p)


def main() -> int:
    ap = argparse.ArgumentParser(description="Install a repo skill and symlink it into agents.")
    ap.add_argument("--skill", default=DEFAULT_SKILL,
                    help="skill dir (relative to the repo) to install (default: %(default)s)")
    ap.add_argument("--agents", default=",".join(DEFAULT_AGENTS),
                    help="comma-separated agents to link (default: %(default)s)")
    ap.add_argument("--hub", default=str(Path.home() / ".agents" / "skills"),
                    help="shared install root (default: %(default)s)")
    ap.add_argument("--link", action="store_true",
                    help="install the hub as a symlink to the repo skill (dev mode) instead of a copy")
    ap.add_argument("--uninstall", action="store_true", help="remove the agent symlinks and the install")
    ap.add_argument("--force", action="store_true", help="overwrite a non-symlink target at an agent path")
    ap.add_argument("--dry-run", action="store_true", help="print actions without changing anything")
    args = ap.parse_args()

    src = (REPO / args.skill).resolve()
    if not (src / "SKILL.md").is_file():
        sys.exit(f"error: {src} is not a skill (no SKILL.md)")
    name = src.name
    hub = Path(args.hub).expanduser() / name
    agents = [a.strip() for a in args.agents.split(",") if a.strip()]
    links = [(a, Path.home() / f".{a}" / "skills" / name) for a in agents]
    DRY = args.dry_run

    def step(msg: str) -> None:
        print(f"  {'[dry-run] ' if DRY else ''}{msg}")

    if args.uninstall:
        print(f"Uninstalling '{name}'")
        for _, link in links:
            if link.is_symlink():                      # a per-skill symlink we created -> remove just the link
                step(f"remove symlink {link}")
                if not DRY:
                    link.unlink()
            elif link.exists() and link.resolve() == hub.resolve():
                step(f"{link} resolves to the hub — removed with it")
            elif link.exists():
                step(f"leave {link} — not a symlink this installer created")
        if hub.is_symlink() or hub.exists():           # rm() unlinks a --link hub, rmtrees a copied one
            step(f"remove {hub}")
            if not DRY:
                rm(hub)
        print("Done.")
        return 0

    # 1) install into the hub
    print(f"Installing '{name}' ({src})  ->  {hub}  ({'symlink to repo' if args.link else 'copy'})")
    if not DRY:
        hub.parent.mkdir(parents=True, exist_ok=True)
    if hub.is_symlink() or hub.exists():
        step(f"replace existing {hub}")
        if not DRY:
            rm(hub)
    if args.link:
        step(f"symlink {hub} -> {src}")
        if not DRY:
            hub.symlink_to(src, target_is_directory=True)
    else:
        step(f"copy {src} -> {hub}")
        if not DRY:
            shutil.copytree(src, hub)

    # 2) symlink into each selected agent
    for agent, link in links:
        print(f"Agent '{agent}':")
        if link.exists() and link.resolve() == hub.resolve():
            step(f"already available — {link} resolves to the hub")
            continue
        if not DRY:
            link.parent.mkdir(parents=True, exist_ok=True)
        if link.is_symlink():
            step(f"refresh symlink {link}")
            if not DRY:
                rm(link)
        elif link.exists():
            if not args.force:
                step(f"skip {link} — exists and is not a symlink (use --force)")
                continue
            step(f"overwrite {link}")
            if not DRY:
                rm(link)
        step(f"symlink {link} -> {hub}")
        if not DRY:
            link.symlink_to(hub, target_is_directory=True)

    print(f"Done. '{name}' installed at {hub}; linked into: {', '.join(agents)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
