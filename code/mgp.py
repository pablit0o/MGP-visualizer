import requests
import json
import sys

from getpass import getpass

"""
Some of the code provided is sample code
from the MGP API. To access it please visit [1*].
"""

PROTOCOL = "https"
HOSTNAME = "mathgenealogy.org"
PORT = "8000"
DATA = 'data/mgp_data.json'

def getlogin():
    print("Enter email used for MGP authentication:",end=" ",file=sys.stderr)
    email = input()
    password = getpass()
    return {'email': email, 'password': password}

def login(authdata):
    r = requests.post(f"{PROTOCOL}://{HOSTNAME}:{PORT}/login", authdata)
    if r.ok:
        r.close()
        return r.json()
    else:
        r.close()
        raise RuntimeError("Failed to authenticate")
    
def doquery(endpoint,token,params):

    headers = {'x-access-token': token['token']}
    r = requests.get(f"{PROTOCOL}://{HOSTNAME}:{PORT}{endpoint}",headers=headers, params=params)
    if r.ok:
        data = r.json()
        r.close()
        return data
    else:
        r.close()
        raise RuntimeError("Error executing query")

if __name__ == '__main__':
    """
    ALL 
    https://mathgenealogy.org:8000/api/v2/MGP/acad/all/

    ONE ID (["advised by"],["advisees"])
    https://mathgenealogy.org:8000/api/v2/MGP/acad?id=[number]

    **GRAPH NEIGHBORS!!! (yes!!)
    https://mathgenealogy.org:8000/api/v2/MGP/graph/neighbors?id=[number]

    **EDGES!! (bfs heaven!)
    https://mathgenealogy.org:8000/api/v2/MGP/graph/edges/
    """

    # [FN1]
    authdata = getlogin()
    token = login(authdata)
    endpoint = '/api/v2/MGP/acad/all'

    # as of 22/06/2026: 346140 IDs
    ID_all = doquery(endpoint,token,params='')
    endpoint = '/api/v2/MGP/acad'

    # o(n) but takes a long time [2*]
    for ID in ID_all:
        querydata = {"id" : str(ID)}
        info = json.dumps(doquery(endpoint,token,querydata))

        with open(DATA,'a') as file:
            file.write(info + '\n')
