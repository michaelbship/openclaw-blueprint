#!/usr/bin/env python3
"""
Deploy config changes: backup, update, restart gateway.

Usage:
    python3 deploy_config.py --provider-json '{"name":"groq",...}' --api-key KEY
    python3 deploy_config.py --provider-json '...' --api-key KEY --aliases '{...}'
    python3 deploy_config.py --provider-json '...' --api-key KEY --dry-run
"""

import subprocess
import sys
import os
import argparse
import time
import json
from pathlib import Path

DEFAULT_CONFIG = Path.home() / ".openclaw" / "openclaw.json"


def run_script(script_name: str, args: list) -> subprocess.CompletedProcess | None:
    """Run a sibling script."""
    script_path = Path(__file__).parent / script_name
    if not script_path.exists():
        print(f"ERROR: Script not found: {script_path}")
        return None
    cmd = ["python3", str(script_path)] + args
    return subprocess.run(cmd, capture_output=True, text=True)


def restart_gateway() -> bool:
    """Restart the OpenClaw gateway service."""
    print("Restarting gateway...")
    result = subprocess.run(
        ["systemctl", "--user", "restart", "openclaw-gateway"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"RESTART_WARNING: {result.stderr}")

    time.sleep(3)
    result = subprocess.run(
        ["systemctl", "--user", "is-active", "openclaw-gateway"],
        capture_output=True,
        text=True,
    )
    if "active" in result.stdout:
        print("GATEWAY_ACTIVE: Service is running")
        return True
    else:
        print(f"GATEWAY_STATUS: {result.stdout.strip()}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Deploy config changes")
    parser.add_argument("--provider-json", required=True, help="JSON provider config")
    parser.add_argument("--api-key", required=True, help="API key")
    parser.add_argument("--aliases", help="JSON aliases")
    parser.add_argument("--config-path", default=str(DEFAULT_CONFIG))
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    try:
        provider_data = json.loads(args.provider_json)
        display_name = provider_data.get("name", "custom")
    except json.JSONDecodeError:
        display_name = "custom"

    print("=" * 60)
    print("CONFIG DEPLOYMENT")
    print(f"Provider: {display_name}")
    print(f"Config: {args.config_path}")
    print("=" * 60)

    if args.dry_run:
        print(f"\nDRY RUN — Would:")
        print(f"  1. Backup config")
        print(f"  2. Add provider '{display_name}'")
        print(f"  3. Restart gateway")
        return 0

    # Phase 1: Backup
    print("\n--- PHASE 1: BACKUP ---")
    result = run_script("backup_config.py", ["--config-path", args.config_path])
    if not result or "BACKUP_SUCCESS" not in result.stdout:
        print("DEPLOY_ABORTED: Backup failed")
        if result:
            print(result.stdout)
        return 1
    print(result.stdout)

    # Phase 2: Update
    print("\n--- PHASE 2: UPDATE ---")
    update_args = [
        "--provider-json",
        args.provider_json,
        "--api-key",
        args.api_key,
        "--config-path",
        args.config_path,
    ]
    if args.aliases:
        update_args.extend(["--aliases", args.aliases])

    result = run_script("update_config.py", update_args)
    if not result or (
        "UPDATE_COMPLETE" not in result.stdout and "NO_CHANGES" not in result.stdout
    ):
        print("DEPLOY_ABORTED: Update failed")
        if result:
            print(result.stdout)
        return 1
    print(result.stdout)

    # Phase 3: Restart
    print("\n--- PHASE 3: RESTART ---")
    restart_gateway()

    print("\n" + "=" * 60)
    print("DEPLOYMENT COMPLETE")
    print("=" * 60)
    return 0


if __name__ == "__main__":
    sys.exit(main())
