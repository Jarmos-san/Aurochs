import requests


def get_request(url):
    r = requests.get(url)
    return r
