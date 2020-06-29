import socket
import helpers

class Client:
    '''A class for initializing a client
    '''

    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port

    def connect(self):
        '''Open socket and connect to the HOST via PORT
        '''

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.connect((self.HOST, self.PORT))
        print(f'Connection established to: {(self.HOST, self.PORT)}')

        message_from_server = helpers.receive(self.server_socket)
        if message_from_server:
            print(message_from_server)
            return
        else:
            return

    def disconnect(self):
        '''Close active connection both server-side and client-side
        '''

        if not hasattr(self, 'server_socket'):
            print('No connection active')
            return

        helpers.send_message(self.server_socket, 'bye bye')
        self.server_socket.close()
        print(f'Connection to {(self.HOST, self.PORT)} closed')      

# ----------------------------------------

client = Client('127.0.0.1', 61235)
client.movie_database = helpers.csv_to_dict('C:/Users/ruben/OneDrive/Projects/mercury/input/movies.csv', sep='\t')

client.connect()
client.disconnect()