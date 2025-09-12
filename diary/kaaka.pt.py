

import subprocess

def run_program(port, filename):
    cmd = ["mpremote", "connect", port, "run", filename]
    subprocess.run(cmd)

run_program("COM4", "C:\\Users\\isami\\OneDrive\\Desktop\\myproject\\user_program.py")
