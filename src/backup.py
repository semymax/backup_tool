from pathlib import Path
import tarfile
import tempfile

def create_tar(sources: list[Path], extra_files: list[Path] | None = None) -> Path:
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".tar")
    tar_path = Path(temp_file.name)

    with tarfile.open(tar_path, "w") as tar:
        for src in sources:
            tar.add(src, arcname=src.name)
            
        if extra_files:
            for f in extra_files:
                tar.add(f, arcname=f.name)
        
    return tar_path
