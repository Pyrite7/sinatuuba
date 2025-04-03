from yt_dlp import YoutubeDL




def get_download_options(music_path: str) -> dict:
    return {
        'format': 'm4a/bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
        }],
        'paths': {'home': music_path},
        'download_archive': music_path + '/downloaded.txt'
    }



def create_download_url(video_id: str) -> str:
    return 'https://www.youtube-nocookie.com/embed/' + video_id



def download_song(video_id: str, music_path: str) -> int:
    with YoutubeDL(get_download_options(music_path)) as ydl:
        exit_code = ydl.download(create_download_url(video_id))
        return exit_code



