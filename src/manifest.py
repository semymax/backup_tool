from pathlib import Path
from datetime import datetime, timezone
import json

def create_manifest(
    sources: list[Path],
    compression: str,
    level: int,
    tool_name: str,
    tool_version: str
) -> dict:
    return {
        "manifest_version": 1,
        "tool": {
            "name": tool_name,
            "version": tool_version
        },
        "created_at": datetime.now(timezone.utc).isoformat(),
        "archive": {
            "format": "tar",
            "compression": "compression",
            "compression_level": level
        },
        "sources": [
            {
                "path": str(p),
                "type": "directory" if p.is_dir() else "file",
            }
            for p in sources
        ],
        "checksum": {
            "algorithm": "sha256"
        }
    }
    
def write_manifest(manifest: dict, dest: Path) -> Path:
    manifest_path = dest / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2))
    return manifest_path
