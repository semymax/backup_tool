from pathlib import Path
import tarfile
import click

class UnsafePathError(Exception):
    pass

def is_within_directory(base: Path, target: Path) -> bool:
    try:
        target.resolve().relative_to(base.resolve())
        return True
    except ValueError:
        return False
    
def safe_extract_tar(tar_path: Path, destination: Path, *, force: bool = False):
    destination = destination.resolve()
    
    with tarfile.open(tar_path, "r") as tar:
        for member in tar.getmembers():
            if member.name == "manifest.json":
                continue
                
            member_path = destination / member.name

            if Path(member.name).is_absolute():
                raise UnsafePathError(
                    f"Absolute path found in tar {member.name}"
                )
                
            if not is_within_directory(destination, member_path):
                raise UnsafePathError(
                    f"Path traversal detected: {member.name}"
                )

            if member.isdir():
                member_path.mkdir(parents=True, exist_ok=True)
                continue
            
            member_path.parent.mkdir(parents=True, exist_ok=True)
            
            if member_path.exists() and not force:
                raise click.UsageError(
                    f"File already exists: {member_path} (use --force)"
                )
                
            with tar.extractfile(member) as src, open(member_path, "wb") as dst:
                if src:
                    dst.write(src.read())
                    
            try:
                member_path.chmod(member.mode)
            except PermissionError:
                pass

def extract_tar(tar_path: Path, destination: Path) -> Path:
    with tarfile.open(tar_path, "r") as tar:
        members = [
            m for m in tar.getmembers()
            if m.name != "manifest.json"
        ]
        tar.extractall(destination, members)
