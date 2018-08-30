from socket import *
socketPort = 12000
serverSocket = socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print("The server is ready to receive")
while Ture:
    message,clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage,clientAddress)
    