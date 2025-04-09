import ipc
import sys
import playlists



def send_fifo_msg(msg: str):
    ipc.send_fifo_msg(msg, "cli2main")


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

        case "skip" | "-s":
            send_fifo_msg("skip")

        case "pause" | "-p":
            send_fifo_msg("pause")

        case "add":
            match len(sys.argv[2:]):
                case 2:
                    playlists.add_to_playlist(sys.argv[2], sys.argv[3])
                case 1:
                    playlists.add_to_favourite_playlist(sys.argv[2])
                case 0:
                    send_fifo_msg("add_current")

        case "remove":
            match len(sys.argv[2:]):
                case 2:
                    playlists.remove_from_playlist(sys.argv[2], sys.argv[3])
                case 1:
                    playlists.remove_from_favourite_playlist(sys.argv[2])
                case 0:
                    send_fifo_msg("remove_current")

        case "new":
            playlists.create_playlist(sys.argv[2])

        case "fav":
            playlists.set_favourite_playlist(sys.argv[2])

        case "quit":
            send_fifo_msg("quit")




