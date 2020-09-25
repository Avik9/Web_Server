# Avik Kadakia
# akadakia
# 111304945
# 
# CSE 310
# PA 1

#import socket module
from socket import *
import threading
import sys # In order to terminate the program
import time

SERVER_NAME = 'localhost'
SERVER_PORT = 12000

def start_server():

    threads = []

    # Prepare a server socket
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((SERVER_NAME, SERVER_PORT))
    serverSocket.listen(5000)

    while True:
        #Establish the connection
        
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()

        try:
            t = threading.Thread(target = client_handler, args = (connectionSocket, addr))
            threads.append(t)
            t.start()
        
        except KeyboardInterrupt:
            connectionSocket.close()

def client_handler(connectionSocket, addr):
    outputdata = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"

    try:
        message = connectionSocket.recv(4096).decode()
        print("Message:", message)

        if not message or " " not in message:
            raise IOError

        filename = message.split()[1]
        # print("filename:", filename)

        f = open(filename[1:])
        outputdata += f.read()
        f.close()

        outputdata += "\r\n"

        # time.sleep(2)

        connectionSocket.send(outputdata.encode())
        connectionSocket.close()

    except IOError:
        # Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        
        #Close client socket
        connectionSocket.close()

if __name__ == "__main__":
    start_server()