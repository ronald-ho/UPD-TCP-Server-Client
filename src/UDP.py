import json
import socket

class UDP():

    def __init__(self, serverHost, serverPort):
        self.serverAddress = (serverHost, serverPort)

    def connect(self):
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.serverSocket.bind(self.serverAddress)

    def receive(self):
        request, address = self.serverSocket.recvfrom(1024)
        self.clientAddress = address

        return json.loads(request.decode())

    def send(self, response):
        self.serverSocket.sendto((bytes(json.dumps(response).encode())), self.clientAddress)

    def close(self):
        self.serverSocket.close()