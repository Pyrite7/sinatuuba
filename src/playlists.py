import os
import config





def format_filename(playlist_name: str) -> str:
    return playlist_name + config.PLAYLIST_FILE_EXTENSION


def format_full_path(playlist_name: str, playlist_path: str) -> str:
    return os.path.join(playlist_path, playlist_name + config.PLAYLIST_FILE_EXTENSION)


def get_all_playlist_files(playlist_path: str) -> list:
    return [file for file in os.listdir(playlist_path) if os.path.isfile(os.path.join(playlist_path, file))]


def get_all_playlists(playlist_path: str) -> list:
    files = [file for file in os.listdir(playlist_path) if os.path.isfile(os.path.join(playlist_path, file))]
    return list(map(lambda filename: filename.removesuffix(config.PLAYLIST_FILE_EXTENSION), files))


def playlist_exists(name: str, playlist_path: str) -> bool:
    return name in get_all_playlists(playlist_path)








def load_playlist(name: str, playlist_path: str) -> list:
    full_path = format_full_path(name, playlist_path)
    
    if playlist_exists(name, playlist_path):
        with open(full_path, 'r') as file:
            raw = file.readlines()
            filtered = filter(lambda line: line != '\n', raw)
            return list(map(lambda line: line.rstrip(), filtered))
        return None
    return None


def unsafe_write_playlist(contents: list, name: str, playlist_path: str):
    """
    DO NOT USE DIRECTLY !!!!!!
    Writes a list of videoIDs to the playlist file of a given name.
    If the file doesn't exist, create it, OTHERWISE OVERWRITE THE CONTENTS OF THE PLAYLIST!!!!
    """
    full_path = format_full_path(name, playlist_path)

    with open(full_path, 'w') as file:
        for video_id in contents:
            file.write(video_id + '\n')


def add_to_playlist(video_id: str, playlist_name: str, playlist_path: str):
    if playlist_exists(playlist_name, playlist_path):
        contents = load_playlist(playlist_name, playlist_path)
        contents.append(video_id)
        unsafe_write_playlist(contents, playlist_name, playlist_path)


def remove_from_playlist(video_id: str, playlist_name: str, playlist_path: str):
    if playlist_exists(playlist_name, playlist_path):
        contents = load_playlist(playlist_name, playlist_path)
        contents.remove(video_id)
        unsafe_write_playlist(contents, playlist_name, playlist_path)





def create_playlist(name: str, playlist_path: str):
    open(format_full_path(name, playlist_path), 'w')


def delete_playlist(name: str, playlist_path: str):
    """NOTE: only works if the playlist is empty!!!"""
    contents_or_none = load_playlist(name, playlist_path)
    if contents_or_none == []:
        os.remove(format_full_path(name, playlist_path))


