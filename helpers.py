import pandas as pd

def csv_to_dict(input_file, sep=';'):
    '''Transforms *.csv-file input into dictionary using the pandas module
    '''
    data = {}
    df = pd.read_csv(input_file, sep)
    df = df.fillna('')

    for column in list(df.columns):
        data[column] = df[column].tolist()

    return data