import socket, sys, errno
from datetime import datetime

remoteServer = input("Enter a remote host to scan:")
remoteServerIP = socket.gethostbyname(remoteServer)

print("Enter the range of ports you would like to scan:")
startPort = input("Starting port:")
endPort = input("End port:")

print("Scanning remote host. Please wait.", remoteServerIP)

time_init = datetime.now()

try:
    for port in range(int(startPort), int(endPort)):
        print("Checking port {} ...".format(port))
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}: Open".format(port))
        else:
            print("Port {}: Closed".format(port))
            print("Reason:",errno.errorcode[result])
        sock.close()

except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved. Exiting.")
    sys.exit()
except socket.error:
    print("Couldn't connect to server.")
    sys.exit()

time_finish = datetime.now()
total = time_finish - time_init
print("Port scanning completed in: ", total)
