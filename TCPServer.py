from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
server.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to Receive')
while 1:
    connectionSocket,addr = serverSocket.accpet()
    sentence = connectionSocket.recv(1024)
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence)
    connectionSocket.close()