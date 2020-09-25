# Avik Kadakia
# akadakia
# 111304945
# 
# CSE 310
# PA 1

from socket import *
import sys

SERVER_NAME = 'localhost'
SERVER_PORT = 12000

def run_client(server_name, server_port, filename):
    client_socket = socket(AF_INET, SOCK_STREAM)

    try:
        client_socket.connect((server_name, server_port))
        message = "GET /" + filename + " HTTP/1.1\r\nConnection: keep-alive\r\n\r\n"

        client_socket.send(message.encode())
        recieved_message = client_socket.recv(4096)

        print("Message Recieved:", recieved_message)

    except error:
        print("Conection to", server_name, "on port", server_port, "has been refused")

    client_socket.close()
    
if __name__ == "__main__":
    sn = sys.argv[1] if len(sys.argv) > 1 else SERVER_NAME
    sp = int(sys.argv[2]) if len(sys.argv) > 2 else SERVER_PORT
    sf = sys.argv[3] if len(sys.argv) > 3 else "HelloWorld.html"

    run_client(sn, sp, sf)