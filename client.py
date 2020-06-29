import socket
import helpers
import json

class Client:
    '''A class for initializing a client
    '''

    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port
        self.data = {}

    def connect(self):
        '''Open socket and connect to the HOST via PORT
        '''

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.connect((self.HOST, self.PORT))
        print(f'Connection established to: {(self.HOST, self.PORT)}')

        message_from_server = helpers.receive(self.server_socket)
        if message_from_server == 'No data available':
            print(f'{self.server_socket.getpeername()}: {message_from_server}')
            return
        else:
            self.data = json.loads(message_from_server)
            return

    def disconnect(self):
        '''Close active connection both server-side and client-side
        '''

        if not hasattr(self, 'server_socket'):
            print('No connection active')
            return

        self.server_socket.close()
        print(f'Connection to {(self.HOST, self.PORT)} closed')

    def import_database(self, input_file, database_name='new_database'):
        self.connect()
        
        self.data[f'{database_name}'] = helpers.csv_to_dict(input_file, sep='\t')
        helpers.send_data(self.server_socket, self.data)

        self.disconnect()
        return        

# ----------------------------------------

client = Client('127.0.0.1', 61235)

client.connect()
client.disconnect()

client.import_database('C:/Users/ruben/OneDrive/Projects/mercury/input/movies.csv')

client.connect()
print(client.data)
client.disconnect()

