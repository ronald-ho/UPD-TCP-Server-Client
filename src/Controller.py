import socket
import sys

from src.server.Server import SERVER_HOST

def main():

    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 server.py <server_port>")
        exit(0)

    serverPort = int(sys.argv[1])
    serverAddress = (SERVER_HOST, serverPort)

    # Set up the server socket
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(serverAddress)