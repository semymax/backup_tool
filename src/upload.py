import subprocess
from pathlib import Path

def upload_rclone(file_path: Path, remote: str):
    cmd = [
        "rclone",
        "copy",
        str(file_path),
        remote,
        "--progress",
    ]
    
    subprocess.run(cmd, check=True)
