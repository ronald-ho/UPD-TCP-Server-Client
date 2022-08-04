import socket

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
            fileData = clientSocket.recv(1024)
            while fileData:
                recvFile.write(fileData)
                fileData = clientSocket.recv(1024)

    def sendFileTCP(self, filename, clientSocket):
        with open(filename, 'rb') as sendFile:
            fileData = sendFile.read(1024)
            while fileData:
                clientSocket.send(fileData)
                fileData = sendFile.read(1024)

    def closeTCP(self):
        self.serverSocket.close()