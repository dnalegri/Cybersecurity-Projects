import socket
print("Creating socket...")
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Socket created.")
print("Connection with remote host...")

target_host = "www.google.com"
target_port = 80

sock.connect((target_host,target_port))
print("Connection ok.")

request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % target_host
sock.send(request.encode())

data = sock.recv(4096)
print("Data",str(bytes(data)))
print("Length",len(data))


print("Closing the socket...")
sock.close()
