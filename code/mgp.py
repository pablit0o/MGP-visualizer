import requests
import json
import sys

from getpass import getpass

"""
Some of the code provided is sample code
from the MGP API. To access it please refer to [1*].
"""

PROTOCOL = "https"
HOSTNAME = "mathgenealogy.org"
PORT = "8000"
DATA = 'data/mgp_data.json'

def getlogin():
    """Get login of user.
    
    args:
        null

    returns:
        A dict consisting of user's PII.
    """
    print("Enter email used for MGP authentication:",end=" ",file=sys.stderr)
    email = input()
    password = getpass()
    return {'email': email, 'password': password}

def login(authdata):
    """Use login data to access MGP API.

    args:
        authdata: dict with two entries email and password
    
    returns:
        json-format of the account data; raises RuntimeError else
    """
    r = requests.post(f"{PROTOCOL}://{HOSTNAME}:{PORT}/login", authdata)
    if r.ok:
        r.close()
        return r.json()
    else:
        r.close()
        raise RuntimeError("Failed to authenticate")
    
def doquery(endpoint,token,params):
    """Queries for the MGP API data.
    
    args:
        endpoint: Specified filepath for MGP API.
        token: Unique token to verify query is from a user.
        params: Specific IDs, ranges, etc. to modify/specify query.
    
    returns:
        json-format of the API data; raises RuntimeError else
    """
    headers = {'x-access-token': token['token']}
    r = requests.get(f"{PROTOCOL}://{HOSTNAME}:{PORT}{endpoint}",headers=headers, params=params)
    if r.ok:
        data = r.json()
        r.close()
        return data
    else:
        r.close()
        raise RuntimeError("Error executing query")
            
    
def main(cont=0):
    """
    ALL 
    https://mathgenealogy.org:8000/api/v2/MGP/acad/all/

    ONE ID (["advised by"],["advisees"])
    https://mathgenealogy.org:8000/api/v2/MGP/acad?id=[number]

    **GRAPH NEIGHBORS
    https://mathgenealogy.org:8000/api/v2/MGP/graph/neighbors?id=[number]

    **EDGES (bfs)
    https://mathgenealogy.org:8000/api/v2/MGP/graph/edges/
    """
    # [1*]
    authdata = getlogin()
    token = login(authdata)
    endpoint = '/api/v2/MGP/acad/all'

    # as of 22/06/2026: 346140 IDs
    ID_all = doquery(endpoint,token,params='')
    endpoint = '/api/v2/MGP/acad'

    if cont == 0:
        with open(DATA,'a') as file:
            file.write('[\n')

    # o(n) but takes a long time [2*]
    with open(DATA,'a') as file:
        for entry in range(cont,len(ID_all)+1): # inclusive
                querydata = {"id" : str(ID_all[entry])}

                # Had to brute force impl but works
                json.dump(doquery(endpoint,token,querydata),file)
                if entry != len(ID_all):
                    file.write(',\n')
                else:
                    file.write('\n]')

if __name__ == '__main__':
    # Please don't do a while loop. If possible, query the data manually. You will get a runtime error roughly every two hours.
    main(276244)