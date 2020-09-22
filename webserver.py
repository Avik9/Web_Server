#import socket module
from socket import *
import sys # In order to terminate the program

SERVER_NAME = 'localhost'
SERVER_PORT = 12009

# Prepare a server socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((SERVER_NAME, SERVER_PORT))
serverSocket.listen(5000)

while True:

    #Establish the connection

    print('Ready to serve...')
    clientSocket, addr = serverSocket.accept()

    outputdata = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
    f = None

    try:
        message = clientSocket.recv(4096).decode()
        if not message:
            raise IOError

        filename = message.split()[1]
        print("Filename:", filename)
        f = open(filename[1:])
        outputdata += f.read()
        f.close()

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            clientSocket.send(outputdata[i].encode())
        clientSocket.send("\r\n".encode())

        clientSocket.close()
        

    except IOError:
        # Send response message for file not found
        clientSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        
        #Close client socket
        clientSocket.close()

serverSocket.close()

sys.exit() # Terminate the program after sending the corresponding data