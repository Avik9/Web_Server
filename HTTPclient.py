# Avik Kadakia
# akadakia
# 111304945
# 
# CSE 310
# PA 1

from socket import *
import sys

SERVER_NAME = 'localhost'
SERVER_PORT = 12010

def run_client(server_name, server_port, filename):
    client_socket = socket(AF_INET, SOCK_STREAM)
    
    client_socket.connect((server_name, server_port))
    message = "GET /" + filename + " HTTP/1.1\r\nConnection: keep-alive\r\n\r\n"

    for i in range(0, len(message)):
        client_socket.send(message[i].encode())
    client_socket.send("\r\n".encode())

    recieved_message = client_socket.recv(4096).decode()
    print("Message recieved:", recieved_message)

    print("From Server:", recieved_message.decode())
    print("AT:", client_socket.getpeername())
    client_socket.close()

    
    # client_socket.connect((server_name, server_port))
    # message = "GET /" + filename + " HTTP/1.1\r\n\r\n"
    # client_socket.send(message.encode())
    # response = client_socket.recv(409600)
    # print("From Server:", response.decode())
    # print("AT:", client_socket.getpeername())
    # client_socket.close()
    
if __name__ == "__main__":
    sn = sys.argv[1] if len(sys.argv) > 1 else SERVER_NAME
    sp = int(sys.argv[2]) if len(sys.argv) > 2 else SERVER_PORT
    sf = sys.argv[3] if len(sys.argv) > 3 else "HelloWorld.html"

    run_client(sn, sp, sf)