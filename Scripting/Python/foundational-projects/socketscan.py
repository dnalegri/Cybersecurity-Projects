import socket, sys

def checkportssocket(ip,portlist):
    try:
        for port in portlist:
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print("Port{}: \t Open".format(port))
            else:
                print("Port{}: \t Closed".format(port))
            sock.close()
    except socket.error as error:
        print(str(error))
        print("Connection error")
        sys.exit()

checkportssocket("localhost",[21,22,23,25,110,143])
