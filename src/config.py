from dotenv import load_dotenv
import os


# === GENERAL CONFIG === #

PLAYLIST_FILE_EXTENSION = '.playlist'







# === ENV VARIABLES === #
load_dotenv()


FILE_PATH = os.getenv("FILE_PATH")
CODE_PATH = os.getenv("CODE_PATH")


PYTHON3_PATH = os.path.join(CODE_PATH, "venv/bin/python3")

def get_script_path(script_name: str) -> str:
    return os.path.join(CODE_PATH, "src", script_name)


MUSIC_PATH = os.path.join(FILE_PATH, "Music")
YTDLP_ARCHIVE = os.path.join(FILE_PATH, "downloaded.txt")

def get_playlist_path(playlist_name: str) -> str:
    return os.path.join(FILE_PATH, "Playlists", playlist_name + PLAYLIST_FILE_EXTENSION)


def get_fifo_path(fifo_name: str) -> str:
    return os.path.join(FILE_PATH, "Ipc", fifo_name)











