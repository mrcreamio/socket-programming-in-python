from socket import *
serverName = 'localhost'
serverPort = 7000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input("client:: enter the message to send to server")
clientSocket.sendto(message.encode(),(serverName,serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()