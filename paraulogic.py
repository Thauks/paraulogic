import pandas as pd
import numpy as np

def fits_must(word, must:list, disjunct) -> bool:
    must_ok = False
    if word == np.nan:
        return False
    for letter in word:
        if letter in disjunct:
            return False
        elif letter in must:
            must_ok = True
    return must_ok

def solver(df:pd.DataFrame, must:list, could:list) -> list:
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    disjunct = [x for x in abc if x not in (must + could)]
    df[0].fillna(value='', inplace=True)
    df['sol'] = df[0].apply(lambda x : fits_must(x, must, disjunct))
    return df[df['sol'] == True][0].tolist()

def read_data(filename: str) -> pd.DataFrame:
    return pd.read_csv(filename, header=None)

if  __name__ == '__main__':
    
    # Url
    url = "https://vilaweb.cat/paraulogic/"
        
    # Initialize data and params
    path = './DANOSC.txt'
    df = read_data(path)
    must = ['G']
    could = ['A', 'C', 'I', 'L', 'M', 'R']    
    
    # Finding the solution
    solution = solver(df, must, could)
    solution.sort(key=len, reverse=True)
    print(solution)

    #TODO: Going to the web and start checking the solution
    