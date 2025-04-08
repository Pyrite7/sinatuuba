import config





def send_fifo_msg(msg: str, fifo_name: str):
    with open(config.get_fifo_path(fifo_name), 'w') as fifo:
        fifo.write(msg)
        fifo.flush()



def run_with_fifo_listener(msg_handler, fifo_name: str):
    "Calls listen_fifo in a loop. If there is a message, call msg_handler with it. If msg_handler returns True, exits."
    with open(config.get_fifo_path(fifo_name), 'r') as fifo:
        quit = False
        while not quit:
            msg = fifo.readline()
            if msg:
                quit = msg_handler(msg)


