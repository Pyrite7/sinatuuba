import playback
import config
import sys
import playlists
import random
import vlc
import ipc



with open(config.get_fifo_path("cli2main"), "r") as fifo:
    current_video_id: str = None
    player: vlc.MediaPlayer = None

    current_playlist: list = None
    current_playlist_index: int = None

    
    def play(video_id: str):
        global player, current_video_id
        if player != None:
            player.release()

        current_video_id = video_id
        player = playback.download_and_play(video_id)
    

    while True:
        msg = fifo.readline()
        parts = msg.split(":")
        
        match parts[0]:
            case "play_song":
                play(parts[1])

            case "play_playlist":
                current_playlist = playlists.load_playlist(parts[1])
                random.shuffle(current_playlist)
                current_playlist_index = 0
                play(current_playlist[current_playlist_index])

            case "skip":
                current_playlist_index += 1
                if current_playlist_index >= len(current_playlist):
                    random.shuffle(current_playlist)
                    current_playlist_index = 0
                play(current_playlist[current_playlist_index])

            case "pause":
                if player != None:
                    player.pause()
            
            case "repeat":
                play(current_playlist[current_playlist_index])
            
            case "return_current":
                ipc.send_fifo_msg(current_video_id, "main2cli")

            case "quit":
                sys.exit()
        



