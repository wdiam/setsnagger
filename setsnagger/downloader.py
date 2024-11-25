from pathlib import Path
import subprocess
from typing import List, Tuple
from .utils import extract_video_id, ensure_directory, check_file_exists

class SetDownloader:
    def __init__(self, base_dir: str = '.'):
        """
        Initialize the Set Downloader.
        
        Args:
            base_dir: Base directory for downloads
        """
        self.base_dir = Path(base_dir)
        # Create base directory if it doesn't exist
        ensure_directory(self.base_dir)
    
    def _is_video_processed(self, video_id: str, genre: str) -> bool:
        """Check if video already exists by looking for video_id in filenames."""
        genre_dir = self.base_dir / genre
        return check_file_exists(genre_dir, video_id) if genre_dir.exists() else False
    
    def _get_genre_dir(self, genre: str) -> Path:
        """Get directory for a genre."""
        genre_dir = self.base_dir / genre
        ensure_directory(genre_dir)
        return genre_dir
    
    def _build_download_commands(self, video_url: str, genre: str) -> tuple[list, list]:
        """Build the yt-dlp commands for video and audio download."""
        genre_dir = self._get_genre_dir(genre)
        
        output_template = '%(channel).100s - %(title).100s - %(id)s.%(ext)s'
        
        video_cmd = [
            'yt-dlp',
            '-f', 'bestvideo[height<=1080]+bestaudio',
            '--merge-output-format', 'mkv',
            '-o', str(genre_dir / output_template),
            video_url
        ]
        
        audio_cmd = [
            'yt-dlp',
            '-f', 'bestaudio',
            '--extract-audio',
            '--audio-format', 'mp3',
            '--audio-quality', '0',
            '--postprocessor-args', 'FFmpegExtractAudio:-threads 0 -compression_level 0',
            '-o', str(genre_dir / output_template),
            video_url
        ]
        
        return video_cmd, audio_cmd
    
    def process_single_video(self, video_url: str, genre: str) -> bool:
        """Process a single video URL and its genre."""
        video_id = extract_video_id(video_url)
        
        if self._is_video_processed(video_id, genre):
            print(f"Video {video_id} already processed in genre '{genre}', skipping...")
            return True
            
        print(f"New video {video_id} encountered, processing for genre '{genre}'...")
        
        try:
            video_cmd, audio_cmd = self._build_download_commands(video_url, genre)
            
            subprocess.run(video_cmd, check=True)
            subprocess.run(audio_cmd, check=True)
            
            print(f"Successfully processed {video_id}")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"Error processing video {video_id}: {str(e)}")
            return False
    
    def process_videos(self, video_info: List[Tuple[str, str]]):
        """Process a list of video URLs and their genres."""
        for video_url, genre in video_info:
            self.process_single_video(video_url, genre)