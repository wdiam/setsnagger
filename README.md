# setsnagger

A tool for downloading and organizing music sets. Perfect for DJs and music enthusiasts who want to keep their favorite sets organized by genre (just make sure you have the right permissions to download them).

## Requirements

### System Dependencies
- Python 3.9+
- FFmpeg (used by yt-dlp for media processing)

### Installation

1. Install FFmpeg:
   - Mac: `brew install ffmpeg`
   - Ubuntu/Debian: `sudo apt install ffmpeg`
   - Windows: Download from [FFmpeg website](https://ffmpeg.org/download.html)

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install Python package requirements:
   ```bash
   pip install -r requirements.txt
   ```
   This will install yt-dlp and make it available both as a Python package and command-line tool.

## Usage

See `download_sets.py` for example usage:

```python
from setsnagger import SetDownloader

downloader = SetDownloader(base_dir='music_sets')
videos_to_process = [
    ("https://youtu.be/video1", "techno"),
    ("https://youtu.be/video2", "house")
]
downloader.process_videos(videos_to_process)
```

## Features

- Downloads both video (mkv) and audio (mp3) versions
- Organizes files by genre
- Caps video quality at 1080p for reasonable file sizes
- Skips already processed videos
- Uses multi-threaded processing where available

## Directory Structure

```
music_sets/
├── techno/
│   ├── Channel1 - SetName1 - videoId1.mkv
│   ├── Channel1 - SetName1 - videoId1.mp3
│   └── ...
└── house/
    ├── Channel2 - SetName2 - videoId2.mkv
    ├── Channel2 - SetName2 - videoId2.mp3
    └── ...
```

## Tips
- Original video IDs are preserved in filenames for future reference
- Both video and audio files are stored in the same genre directory
- High-quality audio extraction with multi-threaded processing

## Contributing

Feel free to fork, submit PRs, or suggest improvements!

## License

MIT License - See LICENSE file for details