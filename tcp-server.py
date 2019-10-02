from socket import *
serverPort = 7000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("the server is ready to recieve ")
while True:
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(1024).decode()
    print("message recv from client: ", message)
    message = message.upper()
    connectionSocket.send(message.encode())
    connectionSocket.close()