import requests


def get_imageurls_latest():
    url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    response = requests.get(url)
    response.raise_for_status()
    urls = response.json()['links']['flickr']['original']
    return urls


get_imageurls_latest()