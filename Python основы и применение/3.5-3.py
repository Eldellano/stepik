import requests


def interesting(num):
    url = f'http://numbersapi.com/{num}/math'
    params = {'json': 'true'}
    res = requests.get(url, params=params)
    return res.json()['found']


with open('dataset_24476_3.txt', 'r') as file:
    for line in file:
        if interesting(line.strip()):
            print('Interesting')
        else:
            print('Boring')
