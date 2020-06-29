import pandas as pd
import json

def csv_to_dict(input_file, sep=';'):
    '''Transforms *.csv-file input into dictionary using the pandas module
    '''
    
    data = {}
    df = pd.read_csv(input_file, sep)
    df = df.fillna('')

    for column in list(df.columns):
        data[column] = df[column].tolist()

    return data

def send_message(socket, message, header_size=8):
    '''Send message to socket
    '''

    message = f'{len(message):<{header_size}}{message}'
    socket.send(bytes(message, 'utf-8'))
    return

def send_data(socket, data, header_size=8):
    '''Send data (as json) to socket
    '''

    message = json.dumps(data)
    send_message(socket, message, header_size)
    return    

def receive(socket, buf_size=1024, header_size=8):
    '''Receive all unsent messages from socket
    ''' 

    message_length = socket.recv(8).decode('utf-8')
       
    if message_length:
        message_length = int(message_length)    

        full_message = ''
        while len(full_message) < message_length:
            chunk = socket.recv(buf_size).decode('utf-8')
            full_message += chunk 
        return full_message 
    else:
        print(f'{socket.getpeername()} has closed the connection')
        return