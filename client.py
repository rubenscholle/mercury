import socket
import helpers
import json

class Client:
    '''A class for initializing a client
    '''

    def __init__(self, host, port, header_size=8):
        self.HOST = host
        self.PORT = port
        self.HEADER_SIZE = header_size

    def connect(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.connect((self.HOST, self.PORT))
        print(f'Connection established to: {(self.HOST, self.PORT)}')

    def disconnect(self):
        if hasattr(self, 'server_socket'):
            self.server_socket.send(bytes('bye bye', 'utf-8'))
            self.server_socket.close()
            print(f'Connection to {(self.HOST, self.PORT)} closed')
        else:
            print('No connection active')

    def receive(self, buf_size=1024, header_size=8):
        if not self.server_socket:
            print('No connection has been established yet')
        
        # This bit is a workaround to read the message header but once later on
        new_message = True
        full_message = ''

        while True:
            message = self.server_socket.recv(buf_size).decode('utf-8')
#            This bit is currently not working, because the server is set
#            to blocking mode
#            if message == '':
#                print('The server has nothing new for you')
#                break 

            # This part is to make sure that the full message is received if
            # the message length exceeds the buffer size
            if new_message:
                message_length = int(message[:header_size])
                new_message = False

            full_message += message

            if len(full_message) - header_size == message_length:
                print(f'New message: "{full_message[header_size:]}"')
                break

    def send(self, data):
        if hasattr(self, 'server_socket'):
            message = json.dumps(data)
            message = f'{len(message):<{self.HEADER_SIZE}}{message}'
            self.server_socket.send(bytes(message, 'utf-8'))
            print(f'Message sent to {(self.HOST, self.PORT)}')
        else:
            print('No connection active')            

client = Client('127.0.0.1', 61234)
client.data = helpers.csv_to_dict('C:/Users/ruben/OneDrive/Projects/mercury/input/movies.csv', sep='\t')
client.connect()
client.receive(16)
client.send(client.data)
client.disconnect()