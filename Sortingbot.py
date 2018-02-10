"""########### Python 3.6 #############
import requests

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '155f6a18afbf46b8834bb2a9d8bc91b2',
}

params ={
    # Query parameter
    'q': 'turn on the left light',
    # Optional request parameters, set to default values
    'timezoneOffset': '0',
    'verbose': 'false',
    'spellCheck': 'false',
    'staging': 'false',
}

try:
    r = requests.get("https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/effbf0c9-bdc3-47aa-bd6d-14d032481a1a?subscription-key=155f6a18afbf46b8834bb2a9d8bc91b2&verbose=true&timezoneOffset=0&q=",headers=headers, params=params)
    print(r.json())

except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################"""

import requests

def getSort(content):
    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': '155f6a18afbf46b8834bb2a9d8bc91b2',
    }
    
    params ={
        # Query parameter
        'q': content,
        # Optional request parameters, set to default values
        'timezoneOffset': '0',
        'verbose': 'false',
        'spellCheck': 'false',
        'staging': 'false',
    }
    
    try:
        r = requests.get('https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/effbf0c9-bdc3-47aa-bd6d-14d032481a1a',headers=headers, params=params)
        #print(r.json())
        return(r.json())
    
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))