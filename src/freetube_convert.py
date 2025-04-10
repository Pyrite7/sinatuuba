import playlists
import json
import metadata


def convert_from_freetube(new_playlist_name: str, freetube_playlist_name: str, freetube_file_path: str):
    with open(freetube_file_path, 'r') as file:
        lines = file.readlines()
        jsons = map(lambda line: json.loads(line), lines)
        ftube_playlist = list(filter(lambda j: j["playlistName"] == freetube_playlist_name, jsons))[0]
        
        video_ids = list(map(lambda video: video["videoId"], ftube_playlist["videos"]))

        playlists.unsafe_write_playlist(video_ids, new_playlist_name)



def get_metadata_from_freetube(freetube_playlist_name: str, freetube_file_path: str):
    with open(freetube_file_path, 'r') as file:
        lines = file.readlines()
        jsons = map(lambda line: json.loads(line), lines)
        ftube_playlist = list(filter(lambda j: j["playlistName"] == freetube_playlist_name, jsons))[0]
        
        for entry in ftube_playlist["videos"]:
            metadata.write_video_metadata(entry["videoId"], {
                "title": entry["title"],
                "channel": entry["author"],
            })



