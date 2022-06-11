import requests

def get_funny_fact(day,month):
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }
    response = requests.get(f'http://numbersapi.com/{month}/{day}/date', headers=headers)
    if response.status_code != 200:
        return response.status_code
    else:
        result = response.json()
        return result['text']
    
        

def get_unique_id(day,month):
    return str(day) + str(month)
