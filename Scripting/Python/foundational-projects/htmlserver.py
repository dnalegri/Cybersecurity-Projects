import socket

# define a socket host and port
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8000

# create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
server_socket.bind(((SERVER_HOST,SERVER_PORT)))
server_socket.listen(1)
print("Listening on port %s ..." % SERVER_PORT)

while True:
    # wait for client connections
    client_connection, client_address = server_socket.accept()

    # get client request
    request = client_connection.recv(1024).decode()
    print(request)

    # parse HTTP headers
    headers = request.split("\n")
    filename = headers[0].split()[1]

    # get the content of the file
    if filename == "/":
        filename = "index.html"
    try:
        # get the content of index.html, you will need to create this file
        fin = open(filename) 
        content = fin.read()
        fin.close()

    # send HTTP response
        response = "HTTP/1.0 200 OK\n\n" + content
    except FileNotFoundError:
        response = "HTTP/1.0 404 NOT FOUND\n\n File Not Found"

    client_connection.sendall(response.encode())
    client_connection.close()

# close socket
server_socket.close()
