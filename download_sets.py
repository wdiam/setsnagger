from setsnagger import SetDownloader

def main():
    downloader = SetDownloader(base_dir='music_sets')
    
    videos_to_process = [
        ("https://youtu.be/video1", "techno"),
        ("https://youtu.be/video2", "house")
    ]
    
    downloader.process_videos(videos_to_process)

if __name__ == "__main__":
    main()
