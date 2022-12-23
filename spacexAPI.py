import requests



def get_imageurls_latest(url):

    response = requests.get(url)
    response.raise_for_status()
    urls = response.json()['links']['flickr']['original']
    return urls


print(get_imageurls_latest('https://api.spacexdata.com/v5/launches/latest'))
