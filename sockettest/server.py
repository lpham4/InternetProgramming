import socket

def factorial(n):
    if (n ==1 or n ==0):
        return 1;
    else:
        return n * factorial(n-1)

# Create a socket
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to host and port
socket.bind(("127.0.0.1", 12345))

print("Server is waiting and listening")

# Server listening
while True:
    # Receive from client
    msgClient = socket.recvfrom(2048)
    message = msgClient[0]
    address = msgClient[1]
    msg2 = "Request received from client for factorial: {}".format(message)
    print(msg2)

    # Obtain result from function and attach to response
    try:
        result = factorial(3)
        response = str(result)
    except:
        response = "Error"

    # Sending a reply to client
    dataFromServer = str.encode(response)
    socket.sendto(dataFromServer, address)








