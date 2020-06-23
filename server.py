import socket

HOST = '127.0.0.1'
PORT = 61234

HEADER_LENGTH = 10

def send_msg(socket, msg):
    msg = f'{len(msg):<{HEADER_LENGTH}}' + msg
    socket.send(bytes(msg, 'utf-8'))
    return

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((HOST, PORT))
serversocket.listen(3)

while True:
    clientsocket, address = serversocket.accept()
    print(f'Connection from {address} has been established')
    
    msg = 'Welcome to the Käsekuchen server!'
    msg = f'{len(msg):<{HEADER_LENGTH}}{msg}'
    clientsocket.send(bytes(msg, 'utf-8'))
    
#    msg = 'test'
#    print(msg)
#    msg = f'{len(msg):<{HEADER_LENGTH}}' + msg
#    clientsocket.send(bytes(msg, 'utf-8'))

    msg_from_client = clientsocket.recv(1024)
    if msg_from_client:
        print(f'Received the following message from client {address}:')
        print(msg_from_client.decode('utf-8'))
        if msg_from_client.decode('utf-8') == 'bye bye':
            clientsocket.close()