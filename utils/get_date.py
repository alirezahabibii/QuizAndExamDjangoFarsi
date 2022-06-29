import requests


def iran_time():
    r = requests.get('https://api.keybit.ir/time/')
    json = r.json()
    date = json['date']['full']['official']['iso']['en']  # saat
    return date


