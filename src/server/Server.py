import auth

from RequestHandler import requestHandler
from src.TCP import TCP
from src.UDP import UDP

SERVER_HOST = "127.0.0.1"

class Server():
    
    def __init__(self, serverHost, serverPort):
        self.UDP = UDP(serverHost, serverPort)
        self.TCP = TCP(serverHost, serverPort)
        self.auth = auth.Authenticate()

    def run(self):
        
        while True:
            request = self.UDP.receive()

            serverHandler = requestHandler(request, self.UDP, self.TCP, self.auth)
            serverHandler.run()
