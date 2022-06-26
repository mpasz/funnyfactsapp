from django.forms import model_to_dict
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

def day_validation(day, month):
    if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        max_day = 31
    elif ( month == 4 or month == 6 or month == 9 or month == 11):
        max_day = 30
    elif (month == 2):
        max_day = 29
    return max_day

# def remove_leading_zeros(value):
#     day = [item.lstrip('0') for item in value]
#     without_zeros = []
#     for item in day:
#         if item != '':
#             without_zeros.append(item)
#     return without_zeros


