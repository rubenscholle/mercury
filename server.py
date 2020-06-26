import socket

HOST = '127.0.0.1'
PORT = 61235

HEADER_SIZE = 8

def send_message(socket, message):
    message = f'{len(message):<{HEADER_SIZE}}' + message
    socket.send(bytes(message, 'utf-8'))
    return

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(3)

while True:
    client_socket, address = server_socket.accept()
    print(f'Connection from {address} has been established')
    
    message = 'Welcome to the Käsekuchen server!'
    send_message(client_socket, message)
    
    message_from_client = client_socket.recv(2048).decode('utf-8')
    if message_from_client:
        print(f'Received the following message from client {address}: {message_from_client}')
        if message_from_client == 'bye bye':
            client_socket.close()
            print(f'Connection to {address} closed')
        else:
            data = message_from_client[HEADER_SIZE:]
            send_message(client_socket, data)       