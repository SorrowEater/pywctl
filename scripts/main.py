import subprocess

device = subprocess.check_output("echo iwctl device list", shell=True)
available = subprocess.check_output('echo iwctl network list', shell=True)
prompt = "Please enter your desired station from this list."


def prompt():
    print(prompt)
    print(device)
