import socket
import helpers
import json

HOST = '127.0.0.1'
PORT = 61235

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(3)

data = ''

while True:
    client_socket, address = server_socket.accept()
    print(f'Connection established {address}')
    
    if data:
        helpers.send_data(client_socket, data)
    else:
        helpers.send_message(client_socket, 'No data available')      

    while True:
        message_from_client = helpers.receive(client_socket)
        if not message_from_client:
            client_socket.close()
            print(f'Connection to {address} closed') 
            break
        else:
            print(f'{address}: data received')
            # data = json.loads(message_from_client)