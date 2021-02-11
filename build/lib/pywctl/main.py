import subprocess

device = subprocess.check_output("iwctl device list", shell=True)
help = subprocess.check_output('iwctl help', shell=True)

def setup():
    print(device)
    global ddevice
    ddevice = input("Hey! Enter the Wi-Fi card you want to use from the list: ")

def connect():
    network = input("Enter your SSID here: ")
    passwd = input('Enter your password here: ')
    subprocess.Popen(f'iwctl station', ddevice, 'connect --passphrase', passwd, network, shell=True)

def connectnp():
    network = input("Enter your SSID here: ")
    subprocess.Popen(f'iwctl station', ddevice, 'connect', network, shell=True)
    print(f'iwctl station', ddevice, 'connect', network)

def networks():
    subprocess.Popen(f'iwctl station', ddevice, 'get-networks', shell=True)

def knetworks():
    subprocess.Popen('iwctl known-networks list', shell=True)

def rmknetwork():
    whichone = input('Really? You want to remove a known network? Ok... Which one? ')
    subprocess.Popen(f'known-networks', whichone, 'forget', shell=True)