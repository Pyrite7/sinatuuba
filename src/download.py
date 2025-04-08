from yt_dlp import YoutubeDL
import config



def get_download_options() -> dict:
    return {
        'format': 'm4a/bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
        }],
        'paths': {'home': config.MUSIC_PATH},
        'download_archive': config.YTDLP_ARCHIVE,
    }



def create_download_url(video_id: str) -> str:
    return 'https://www.youtube-nocookie.com/embed/' + video_id



def download_song(video_id: str) -> int:
    with YoutubeDL(get_download_options()) as ydl:
        exit_code = ydl.download(create_download_url(video_id))
        return exit_code



