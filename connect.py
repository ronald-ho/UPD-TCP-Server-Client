import socket
import json

BUFFER_SIZE = 1024

class UDP():

    def __init__(self, serverHost, serverPort):
        self.serverAddress = (serverHost, serverPort)    

    def connectUDP(self):
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.serverSocket.bind(self.serverAddress)

    def receiveUDP(self):
        request, address = self.serverSocket.recvfrom(1024)
        self.clientAddress = address

        return json.loads(request.decode())

    def sendUDP(self, response):
        self.serverSocket.sendto((bytes(json.dumps(response).encode())), self.clientAddress)

    def closeUDP(self):
        self.serverSocket.close()

class TCP():

    def __init__(self, serverHost, serverPort):
        self.serverAddress = (serverHost, serverPort)

    def connectServerTCP(self):
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.bind(self.serverAddress)
        self.serverSocket.listen()
        clientSocket, _ = self.serverSocket.accept()

        return clientSocket

    def connectClientTCP(self):
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientSocket.connect(self.serverAddress)

        return self.clientSocket

    def receiveFileTCP(self, filename, clientSocket):
        with open(filename, 'wb') as recvFile:
            fileData = clientSocket.recv(BUFFER_SIZE)
            while fileData:
                recvFile.write(fileData)
                fileData = clientSocket.recv(BUFFER_SIZE)

    def sendFileTCP(self, filename, clientSocket):
        with open(filename, 'rb') as sendFile:
            fileData = sendFile.read(BUFFER_SIZE)
            while fileData:
                clientSocket.send(fileData)
                fileData = sendFile.read(BUFFER_SIZE)

    def closeTCP(self):
        self.serverSocket.close()