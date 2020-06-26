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
        '''Open socket and connect to the HOST via PORT
        '''

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.connect((self.HOST, self.PORT))
        print(f'Connection established to: {(self.HOST, self.PORT)}')

    def disconnect(self):
        '''Close active connection both server-side and client-side
        '''

        if not hasattr(self, 'server_socket'):
            print('No connection active')
            return

        self.server_socket.send(bytes('bye bye', 'utf-8'))
        self.server_socket.close()
        print(f'Connection to {(self.HOST, self.PORT)} closed')

    def retrieve(self, buf_size=1024, header_size=8):
        '''Retrieve all unsent messages from the HOST
        ''' 
        def get_message_length():
            message_length = int(self.server_socket.recv(8).decode('utf-8'))
            return message_length

        if not hasattr(self, 'server_socket'):
            print('No connection has been established yet')
            return
            
        message_length = get_message_length()            

        full_message = ''
        while len(full_message) < message_length:
            chunk = self.server_socket.recv(buf_size).decode('utf-8')
            full_message += chunk 

        print(f'From {(self.HOST, self.PORT)}: {full_message}')

        return full_message    

    def send_data(self, data):
        '''Send DATA to the HOST
        '''

        if not hasattr(self, 'server_socket'):
            print('No connection has been established yet')
            return

        message = json.dumps(data)
        message = f'{len(message):<{self.HEADER_SIZE}}{message}'
        self.server_socket.send(bytes(message, 'utf-8'))
        print(f'Data sent to {(self.HOST, self.PORT)}')          

client = Client('127.0.0.1', 61235)
client.data = helpers.csv_to_dict('C:/Users/ruben/OneDrive/Projects/mercury/input/movies.csv', sep='\t')
client.connect()
client.retrieve(16)
#client.send_data(client.data)
client.disconnect()