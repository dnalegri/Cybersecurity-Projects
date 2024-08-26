import socket

target_ip = "10.10.10.110"
ports = [80,443,53]

for port in ports:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    result = sock.connect_ex((target_ip,port))
    print(port,":",result)
    sock.close()
