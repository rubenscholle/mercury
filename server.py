import socket
import helpers

HOST = '127.0.0.1'
PORT = 61235

HEADER_SIZE = 8

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(3)

welcome_message = 'Welcome to the Käsekuchen server!'
data = ''

while True:
    client_socket, address = server_socket.accept()
    print(f'Connection from {address} has been established')
    
    if data:
        helpers.send_data(client_socket, data)
    else:
        helpers.send_message(client_socket, welcome_message)      

    message_from_client = helpers.receive(client_socket)
    if not message_from_client:
        print(f'The client {address} has closed the connection')
        client_socket.close()
        print(f'Connection to {address} closed') 
    else:
        print(f'Received the following message from client {address}: {message_from_client}')
        if message_from_client == 'bye bye':
            print(f'The client {address} has closed the connection')
            client_socket.close()
            print(f'Connection to {address} closed')       