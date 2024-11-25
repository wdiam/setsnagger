from pathlib import Path
from typing import Optional


def extract_video_id(url: str) -> str:
    """Extract video ID from YouTube URL."""
    if 'youtu.be/' in url:
        return url.split('youtu.be/')[-1]
    elif 'watch?v=' in url:
        return url.split('watch?v=')[-1]
    return url


def ensure_directory(path: Path) -> Path:
    """Ensure directory exists and return Path object."""
    path.mkdir(parents=True, exist_ok=True)
    return path


def check_file_exists(directory: Path, video_id: str) -> bool:
    """Check if a file containing video_id exists in directory."""
    return any(video_id in f.name for f in directory.glob('*')) if directory.exists() else False
