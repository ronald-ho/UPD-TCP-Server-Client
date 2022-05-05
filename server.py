import sys
import os
import socket

import connect
import auth
import error

SERVER_HOST = "127.0.0.1"

def main():

    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 server.py <server_port>")
        exit(0)

    serverPort = int(sys.argv[1])
    serverAddress = (SERVER_HOST, serverPort)

    # Set up the server socket
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(serverAddress)


class Server():
    
    def __init__(self, serverHost, serverPort):
        self.UDP = connect.UDP(serverHost, serverPort)
        self.TCP = connect.TCP(serverHost, serverPort)
        self.auth = auth.Authenticate()

    def run(self):
        
        while True:
            request = self.UDP.receiveUDP()

            serverHandler = requestHandler(request, self.UDP, self.TCP, self.auth)
            serverHandler.run()

class requestHandler():
    
    def __init__(self, request, UDP, TCP, auth):
        self.request = request
        self.UDP = UDP
        self.TCP = TCP
        self.auth = auth

        self.command = self.request["command"]

    def run(self):
        if self.command == "LOGIN":
            self.serverLOGIN()

        elif self.command == "PASS":
            self.serverPASS()

        elif self.command == "NEW":
            self.serverNEW()

        elif self.command == "CRT":
            self.serverCRT()

        elif self.command == "MSG":
            self.serverMSG()

        elif self.command == "DLT":
            self.serverDLT()

        elif self.command == "EDT":
            self.serverEDT()

        elif self.command == "LST":
            self.serverLST()

        elif self.command == "RDT":
            self.serverRDT()

        elif self.command == "UPD":
            self.serverUPD()

        elif self.command == "DWN":
            self.serverDWN()

        elif self.command == "RMV":
            self.serverRMV()

        elif self.command == "XIT":
            self.serverXIT()  

    def serverLOGIN(self):
        # If the username is already logged in 
        if self.auth.isLoggedIn(self.request["username"]):
            print("User already logged in")
            self.UDP.sendUDP({"status": error.FORBIDDEN})

        # If the username exists
        elif self.auth.usernameExists(self.request["username"]):
            print("Client authenticating")
            self.UDP.sendUDP({"status": error.CONTINUE})

        else:
            self.UPD.sendUDP({"status": error.UNAUTHORIZED})
    
    def serverPASS(self):

        # If the password match the username in the database
        if self.auth.authenticate(self.request["username"], self.request["password"]):
            self.auth.login(self.request["username"])
            print("Client authenticated")
            self.UDP.sendUDP({"status": error.OK})
        
        else:
            print("Incorrect password")
            self.UDP.sendUDP({"status": error.UNAUTHORIZED})

    def serverNEW(self):
        if self.auth.register(self.request["username"], self.request["password"]) == True:
            self.auth.login(self.request["username"])

            print("Client registered")
            self.UDP.sendUDP({"status": error.OK})

        else:
            print("Error creating user")
            self.UDP.sendUDP({"status": error.NOT_FOUND})

    def serverCRT(self):
        

        pass

    def serverMSG(self):
        pass

    def serverDLT(self):
        pass

    def serverEDT(self):
        pass

    def serverLST(self):
        pass

    def serverRDT(self):
        pass

    def serverUPD(self):
        pass

    def serverDWN(self):
        pass

    def serverRMV(self):
        pass

    def serverXIT(self):
        pass

    def createPackage():
        pass

if __name__ == '__main__':
    main()