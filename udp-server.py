from socket import *
serverPort = 7000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print("the server is ready to recieve")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode()
    print("message from client : ", modifiedMessage)
    modifiedMessage = modifiedMessage.upper()

    serverSocket.sendto(modifiedMessage.encode(), clientAddress)