import socket

# Server host and port
serverAddress = ("127.0.0.1", 12345)

# Create a socket
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send to server
msgClient = 3
dataFromClient = bytes([3])
socket.sendto(dataFromClient, serverAddress)

# Receive from server
msgServer = socket.recvfrom(2048)
msg = "Server received request. Message from server. The factorial is: {}".format(msgServer[0])
print(msg)





