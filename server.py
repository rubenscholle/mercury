import socket
import json

HOST = '127.0.0.1'
PORT = 61234

HEADER_SIZE = 8

def send_msg(socket, msg):
    msg = f'{len(msg):<{HEADER_SIZE}}' + msg
    socket.send(bytes(msg, 'utf-8'))
    return

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(3)

while True:
    client_socket, address = server_socket.accept()
    print(f'Connection from {address} has been established')
    
    msg = 'Welcome to the Käsekuchen server!'
    msg = f'{len(msg):<{HEADER_SIZE}}{msg}'
    client_socket.send(bytes(msg, 'utf-8'))
    
#    msg = 'test'
#    print(msg)
#    msg = f'{len(msg):<{HEADER_SIZE}}' + msg
#    client_socket.send(bytes(msg, 'utf-8'))

    msg_from_client = client_socket.recv(2048)
    if msg_from_client:
        print(f'Received the following message from client {address}: {msg_from_client}')
        if msg_from_client.decode('utf-8') == 'bye bye':
            client_socket.close()
        else:
            data = msg_from_client[HEADER_SIZE:].decode('utf-8')
            client_socket.close() 