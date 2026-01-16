from pathlib import Path
import zstandard as zstd

def compress_zstd(tar_path: Path, level: int) -> Path:
    zst_path = tar_path.with_suffix(".tar.zst")
    
    cctx = zstd.ZstdCompressor(level=level)
    
    with open(tar_path, "rb") as fin, open (zst_path, "wb") as fout:
        cctx.copy_stream(fin, fout)
        
    return zst_path
    