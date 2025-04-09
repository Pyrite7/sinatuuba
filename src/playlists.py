import os
import config




def format_filename(playlist_name: str) -> str:
    return playlist_name + config.PLAYLIST_FILE_EXTENSION


def get_playlist_path(playlist_name: str) -> str:
    return os.path.join(config.FILE_PATH, "Playlists", format_filename(playlist_name))


def get_all_playlist_files() -> list:
    return [file for file in os.listdir(config.PLAYLIST_DIRECTORY) if os.path.isfile(os.path.join(config.PLAYLIST_DIRECTORY, file))]


def get_all_playlists() -> list:
    files = get_all_playlist_files()
    return list(map(lambda filename: filename.removesuffix(config.PLAYLIST_FILE_EXTENSION), files))


def playlist_exists(name: str) -> bool:
    return name in get_all_playlists()








def load_playlist(name: str) -> list:
    full_path = get_playlist_path(name)
    
    if playlist_exists(name):
        with open(full_path, 'r') as file:
            raw = file.readlines()
            filtered = filter(lambda line: line != '\n', raw)
            return list(map(lambda line: line.rstrip(), filtered))
        return None
    return None


def unsafe_write_playlist(contents: list, name: str):
    """
    DO NOT USE DIRECTLY !!!!!!
    Writes a list of videoIDs to the playlist file of a given name.
    If the file doesn't exist, create it, OTHERWISE OVERWRITE THE CONTENTS OF THE PLAYLIST!!!!
    """
    full_path = get_playlist_path(name)

    with open(full_path, 'w') as file:
        for video_id in contents:
            file.write(video_id + '\n')


def add_to_playlist(video_id: str, playlist_name: str):
    if playlist_exists(playlist_name):
        contents = load_playlist(playlist_name)
        contents.append(video_id)
        unsafe_write_playlist(contents, playlist_name)


def remove_from_playlist(video_id: str, playlist_name: str):
    if playlist_exists(playlist_name):
        contents = load_playlist(playlist_name)
        contents.remove(video_id)
        unsafe_write_playlist(contents, playlist_name)





def create_playlist(name: str):
    open(get_playlist_path(name), 'w')


def delete_playlist(name: str):
    """NOTE: only works if the playlist is empty!!!"""
    contents_or_none = load_playlist(name)
    if contents_or_none == []:
        os.remove(get_playlist_path(name))



def get_favourite_playlist() -> str:
    with open(os.path.join(config.FILE_PATH, "favourite.txt"), "r") as file:
        return file.readline().strip()

def set_favourite_playlist(name: str):
    with open(os.path.join(config.FILE_PATH, "favourite.txt"), "w") as file:
        file.write(name)

def add_to_favourite_playlist(video_id: str):
    add_to_playlist(video_id, get_favourite_playlist())

def remove_from_favourite_playlist(video_id: str):
    remove_from_playlist(video_id, get_favourite_playlist())
