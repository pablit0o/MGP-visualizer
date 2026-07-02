import pandas as pd
import json # Query manually

DATA = "data/mgp_data.json"

def load(filepath=DATA):
    """Loads a json file
    
    args:
        filepath: filepath of the json file
    
    returns:
        pandas database from json_normalize
    """

    # read_json fails bcs it doesnt expect nested elements
    with open(filepath) as f:
        data = json.load(f)

    df = pd.json_normalize(data)
    return df

def main():
    load()

if __name__ == '__main__':
    main()