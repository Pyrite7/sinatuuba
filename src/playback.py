import vlc
import time
from pathlib import Path
import config


def get_file_from_video_id(video_id: str) -> str:
    for file in Path(config.MUSIC_PATH).rglob(f"*{video_id}*"):
        return str(file)
    return None


def download_and_play(video_id: str) -> vlc.MediaPlayer:
    if get_file_from_video_id(video_id) == None:
        import download
        download.download_song(video_id)
    
    return play(get_file_from_video_id(video_id))


def play(file: str) -> vlc.MediaPlayer:
    player: vlc.MediaPlayer = vlc.MediaPlayer(file)
    player.play()
    time.sleep(2)
    return player


def run_until_finished(player: vlc.MediaPlayer):
    while player.get_state() not in [vlc.State.Ended, vlc.State.Stopped]:
        time.sleep(1)
