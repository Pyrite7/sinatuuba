import config
import subprocess




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


def is_script_running(script_name: str) -> bool:
    result = subprocess.run(
        ["pgrep", "-f", script_name + ".py"]
    )
    return result.returncode == 0


def run_independent(script_name: str, sudo: bool = False):
    """
    Runs the script with the given name as a separate process if
    it isn't running already.
    """
    if is_script_running(script_name):
        return
    
    cmd = [config.PYTHON3_PATH, config.get_script_path(script_name)]
    if sudo:
        cmd.insert(0, "sudo")
    
    subprocess.Popen(
        cmd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        start_new_session=True,
    )


