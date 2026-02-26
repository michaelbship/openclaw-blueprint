#!/usr/bin/env python3
"""
Backup OpenClaw config before making changes.
Creates a timestamped backup of openclaw.json.

Usage:
    python3 backup_config.py [--config-path /path/to/openclaw.json]
"""

import json
import sys
import argparse
from datetime import datetime
from pathlib import Path

DEFAULT_CONFIG = Path.home() / ".openclaw" / "openclaw.json"


def create_backup(config_path: Path) -> str | None:
    """Create a timestamped backup of the config file."""
    if not config_path.exists():
        print(f"ERROR: Config file not found at {config_path}")
        return None

    try:
        with open(config_path, "r") as f:
            config_data = json.load(f)
        print(f"CONFIG_READ: Loaded {config_path}")
    except json.JSONDecodeError as e:
        print(f"ERROR: Config is not valid JSON: {e}")
        return None

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_path = config_path.parent / f"openclaw.json.bak.{timestamp}"

    try:
        with open(backup_path, "w") as f:
            json.dump(config_data, f, indent=2)
        print(f"BACKUP_WRITTEN: {backup_path}")
    except Exception as e:
        print(f"ERROR: Failed to write backup: {e}")
        return None

    # Verify backup
    try:
        with open(backup_path, "r") as f:
            json.load(f)
        print("BACKUP_VALID: Verified as valid JSON")
    except Exception as e:
        print(f"ERROR: Backup verification failed: {e}")
        backup_path.unlink(missing_ok=True)
        return None

    return str(backup_path)


def main():
    parser = argparse.ArgumentParser(description="Backup OpenClaw config")
    parser.add_argument(
        "--config-path",
        default=str(DEFAULT_CONFIG),
        help=f"Config file path (default: {DEFAULT_CONFIG})",
    )
    args = parser.parse_args()

    config_path = Path(args.config_path)
    print("=" * 60)
    print(f"CONFIG BACKUP")
    print(f"Config path: {config_path}")
    print("=" * 60)

    backup_path = create_backup(config_path)
    if backup_path:
        print(f"BACKUP_SUCCESS:{backup_path}")
        return 0
    else:
        print("BACKUP_FAILED")
        return 1


if __name__ == "__main__":
    sys.exit(main())
