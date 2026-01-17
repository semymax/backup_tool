from pathlib import Path
import json

class ConfigError(Exception):
    pass

def load_config(path: Path) -> dict:
    if not path.exists():
        raise ConfigError(f"Config file not found: {path}")
    
    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise ConfigError(f"Invalid JSON: {e}") from e
    
    if data.get("version") != 1:
        raise ConfigError("Unsupported config file version")

    return data
