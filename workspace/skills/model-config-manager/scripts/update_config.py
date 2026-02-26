#!/usr/bin/env python3
"""
Safely update OpenClaw config by adding providers and aliases.

Safety:
    - NEVER overwrites protected keys (tokens, bindings, hooks)
    - Only ADDS providers/aliases, never removes existing ones
    - Validates JSON before writing
    - Creates backup before any changes

Usage:
    python3 update_config.py --provider-json '{"name":"groq","baseUrl":"...","models":[...]}' --api-key KEY
    python3 update_config.py --provider-json '...' --api-key KEY --aliases '{"groq/model":{"alias":"g1"}}'
    python3 update_config.py --provider-json '...' --api-key KEY --dry-run
"""

import json
import sys
import argparse
from pathlib import Path
from datetime import datetime

DEFAULT_CONFIG = Path.home() / ".openclaw" / "openclaw.json"

# These must NEVER be overwritten
PROTECTED_KEYS = [
    "channels.discord.token",
    "channels.telegram.botToken",
    "gateway.auth.token",
    "bindings",
    "hooks",
]

VALID_INPUTS = ["text", "image"]


def check_protected_keys(config: dict) -> None:
    """Warn if config is missing protected keys."""
    missing = []
    for key_path in PROTECTED_KEYS:
        parts = key_path.split(".")
        current = config
        try:
            for part in parts:
                current = current[part]
        except KeyError:
            missing.append(key_path)
    if missing:
        print(f"WARNING: Config missing protected keys: {missing}")


def filter_model_inputs(models: list) -> list:
    """Filter model input modalities to only valid types."""
    for model in models:
        if "input" in model:
            original = model["input"]
            filtered = [i for i in original if i in VALID_INPUTS]
            if filtered != original:
                removed = [i for i in original if i not in VALID_INPUTS]
                print(
                    f"INPUT_FILTERED: {model.get('id', 'unknown')} — removed {removed}"
                )
            model["input"] = filtered
    return models


def add_provider(config: dict, provider_name: str, provider_config: dict) -> bool:
    """Add a new provider. Returns True if added, False if exists."""
    providers = config.setdefault("models", {}).setdefault("providers", {})
    if provider_name in providers:
        print(f"PROVIDER_EXISTS: '{provider_name}' already in config")
        return False
    if "models" in provider_config:
        provider_config["models"] = filter_model_inputs(provider_config["models"])
    providers[provider_name] = provider_config
    count = len(provider_config.get("models", []))
    print(f"PROVIDER_ADDED: '{provider_name}' with {count} models")
    return True


def add_aliases(config: dict, aliases: dict) -> int:
    """Add model aliases. Returns count added."""
    models = (
        config.setdefault("agents", {})
        .setdefault("defaults", {})
        .setdefault("models", {})
    )
    added = 0
    for model_id, alias_config in aliases.items():
        if model_id in models:
            existing = models[model_id].get("alias", "unknown")
            print(f"ALIAS_EXISTS: '{model_id}' -> '{existing}' (skipping)")
            continue
        models[model_id] = alias_config
        print(f"ALIAS_ADDED: '{model_id}' -> '{alias_config.get('alias')}'")
        added += 1
    return added


def validate_config(config: dict) -> bool:
    """Validate config structure before writing."""
    required = ["models", "agents"]
    for key in required:
        if key not in config:
            print(f"VALIDATION_ERROR: Missing required key '{key}'")
            return False
    print("CONFIG_VALID: Structure looks correct")
    return True


def write_config(config: dict, config_path: Path) -> None:
    """Write config atomically."""
    temp_path = config_path.with_suffix(".tmp")
    with open(temp_path, "w") as f:
        json.dump(config, f, indent=2)
    with open(temp_path, "r") as f:
        json.load(f)  # Validate
    temp_path.rename(config_path)
    print(f"CONFIG_WRITTEN: {config_path}")


def create_backup(config_path: Path) -> str:
    """Create timestamped backup."""
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_path = config_path.parent / f"openclaw.json.bak.{timestamp}"
    with open(config_path, "r") as f:
        data = json.load(f)
    with open(backup_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"BACKUP_CREATED: {backup_path}")
    return str(backup_path)


def main():
    parser = argparse.ArgumentParser(description="Safely update OpenClaw config")
    parser.add_argument(
        "--provider-json", required=True, help="JSON string with provider config"
    )
    parser.add_argument("--api-key", required=True, help="API key for the provider")
    parser.add_argument("--aliases", help="JSON string with aliases")
    parser.add_argument(
        "--config-path", default=str(DEFAULT_CONFIG), help="Config file path"
    )
    parser.add_argument("--dry-run", action="store_true", help="Show what would happen")
    args = parser.parse_args()

    config_path = Path(args.config_path)
    provider_data = json.loads(args.provider_json)
    provider_name = provider_data.get("name")

    if not provider_name:
        print("ERROR: Provider JSON must include 'name' field")
        return 1

    aliases = json.loads(args.aliases) if args.aliases else {}
    provider_config = {
        k: v for k, v in provider_data.items() if k not in ("name", "aliases")
    }

    print("=" * 60)
    print(f"CONFIG UPDATE")
    print(f"Config: {config_path}")
    print(f"Provider: {provider_name}")
    print(f"Aliases: {list(aliases.keys()) if aliases else 'none'}")
    print("=" * 60)

    with open(config_path, "r") as f:
        config = json.load(f)

    check_protected_keys(config)

    if args.dry_run:
        print(
            f"\nDRY RUN — Would add provider '{provider_name}' and {len(aliases)} aliases"
        )
        return 0

    backup_path = create_backup(config_path)
    provider_config["apiKey"] = args.api_key

    provider_added = add_provider(config, provider_name, provider_config)
    aliases_added = add_aliases(config, aliases) if aliases else 0

    if not validate_config(config):
        print("VALIDATION_FAILED: Not writing changes")
        return 1

    if provider_added or aliases_added > 0:
        write_config(config, config_path)
        print(f"\nUPDATE_COMPLETE: Provider={provider_added}, Aliases={aliases_added}")
        print(f"BACKUP_SAVED: {backup_path}")
    else:
        print("\nNO_CHANGES: Nothing to update")

    return 0


if __name__ == "__main__":
    sys.exit(main())
