import sys
import os
import socket

import connect
import auth

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
    
    def __init__(self):
        self.UDP = connect.UDP()
        self.TCP = connect.TCP()
        self.auth = auth.Authenticate()

    def run(self):
        
        while True:
            


if __name__ == '__main__':
    main()