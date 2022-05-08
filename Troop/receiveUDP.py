import socket
import sys

class bcolors:
    SVDK = '\033[96m'
    ZBDM = '\033[95m'
    SERVER = '\033[31m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if len(sys.argv) == 3:
    # Get "IP address of Server" and also the "port number" from
    #argument 1 and argument 2
    ip = sys.argv[1]
    port = int(sys.argv[2])
else:
    print("Run like : python3 server.py <arg1:server ip:this system IP 192.168.1.6> <arg2:server port:4444 >")
    exit(1)


# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the port
server_address = (ip, port)
s.bind(server_address)
print("Do Ctrl+c to exit the program !!")
print("####### Server is listening #######")

while True:
    data, address = s.recvfrom(4096)
    datadec = data.decode('utf-8')
    if datadec[0] == "#": # svdk color
        print(f"SVDK: {bcolors.SVDK}{datadec[1:]}")
    elif datadec[0] == "!": # server color
        print(f"ZBDM: {bcolors.ZBDM}{datadec[1:]}")
    elif datadec[0] == "@":
        print(f"SERVER: {bcolors.SERVER}{datadec[1:]}")