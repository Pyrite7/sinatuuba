





def send_fifo_msg(msg: str, fifo_path: str):
    with open(fifo_path, 'w') as fifo:
        fifo.write(msg)
        fifo.flush()


def listen_fifo(fifo) -> str:
    return fifo.readline()


def run_with_fifo_listener(msg_handler, fifo_path: str):
    "Calls listen_fifo in a loop. If there is a message, call msg_handler with it. If msg_handler returns True, exits."
    with open(fifo_path, 'r') as fifo:
        quit = False
        while not quit:
            msg = listen_fifo(fifo)
            if msg:
                quit = msg_handler(msg)


