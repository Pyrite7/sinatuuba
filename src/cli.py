import ipc
import sys
import playlists
import metadata
import config


def send_fifo_msg(msg: str):
    ipc.send_fifo_msg(msg, "cli2main")


def get_current_video_id() -> str:
    send_fifo_msg("return_current")
    with open(config.get_fifo_path("main2cli"), "r") as fifo:
        return fifo.readline().strip()


def format_song_display_name(video_id: str) -> str:
    data = metadata.load_video_metadata(video_id)
    
    channel_name = data["channel"]
    title: str = data["title"]

    if channel_name in title:
        return title + " [" + video_id + "]"
    else:
        return channel_name + " - " + title + " [" + video_id + "]"




if __name__ == "__main__":
    command = None
    
    if len(sys.argv) != 1:
        command = sys.argv[1]
    
    match command:
        case None:
            ipc.run_independent("sinatuuba")
        
        case "play":
            match sys.argv[2]:
                case "-id":
                    send_fifo_msg("play_song:" + sys.argv[3])
                case _:
                    send_fifo_msg("play_playlist:" + sys.argv[2])

        case "skip" | "next":
            send_fifo_msg("skip")

        case "pause":
            send_fifo_msg("pause")
        
        case "repeat":
            send_fifo_msg("repeat")

        case "add":
            match len(sys.argv[2:]):
                case 2:
                    playlists.add_to_playlist(sys.argv[2], sys.argv[3])
                case 1:
                    playlists.add_to_favourite_playlist(sys.argv[2])
                case 0:
                    playlists.add_to_favourite_playlist(get_current_video_id())

        case "remove":
            match len(sys.argv[2:]):
                case 2:
                    playlists.remove_from_playlist(sys.argv[2], sys.argv[3])
                case 1:
                    playlists.remove_from_favourite_playlist(sys.argv[2])
                case 0:
                    playlists.remove_from_favourite_playlist(get_current_video_id())

        case "new":
            playlists.create_playlist(sys.argv[2])

        case "fav":
            playlists.set_favourite_playlist(sys.argv[2])
        
        case "info":
            print(format_song_display_name(get_current_video_id()))

        case "quit":
            send_fifo_msg("quit")




