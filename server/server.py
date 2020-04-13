import socket

# creating a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# taking inputs from user for server and file
server = input("Server: ")
filename = input("Filename: ")

# creating port, path and connecting to server
port = 80
path = "/"
sock.connect((server, port))

# sending requests to server
initial_line="GET "+path+" HTTP/1.1 \n"
header_line="Host: "+server+"\n"
sock.send(initial_line.encode())
sock.send(header_line.encode())
sock.send("\n".encode())

# getting a response back from server and writing into file
response = sock.recvfrom(2048)
file = open(filename, "w")
file.write(str(response))

# print response on terminal
print(response)



