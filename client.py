import socket

HOST = '127.0.0.1'
PORT = 61234

HEADER_LENGTH = 10

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.connect((HOST, PORT))

full_msg = ''
new_message = True

while True:

    msg = server_socket.recv(16)

    if new_message:
        msg_length = int(msg[:HEADER_LENGTH])
        new_message = False

    full_msg += msg.decode('utf-8')
    
    if len(full_msg) - HEADER_LENGTH == msg_length:
        print(full_msg[HEADER_LENGTH:])
        server_socket.send(bytes('bye bye', 'utf-8'))
        break