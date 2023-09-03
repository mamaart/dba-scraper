import requests

def find_person(number):
    url = f'https://www.krak.dk/_next/data/T0lN5V_Qf9hVl0bq5YJ6j/da/search/{number}/persons/1.json'
    r = requests.get(url)
    if r: return r.json()['pageProps']['initialState']['persons']
