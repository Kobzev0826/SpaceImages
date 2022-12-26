import requests
import sys, os


def read_token():
    try:
        token = os.environ["NASA_API"]
    except KeyError as e:
        print(f"Error: {e} \n no token in system environment")
        sys.exit()
    return token


def get_random_images_links(number_of_links, token):
    payload = {"api_key": token, "count": number_of_links}
    url = "https://api.nasa.gov/planetary/apod"
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return [item['url'] for item in response.json()]


def get_epic_links(token):
    url = 'https://api.nasa.gov/EPIC/api/natural'
    payload = {
        "api_key": token,
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()

    urls = []
    for item in response.json():
        date_time = item["date"].split()[0].split('-')
        cur_url = f'https://api.nasa.gov/EPIC/archive/natural/ {"/".join(date_time)}'
        urls.append(f'{cur_url}/png/{item["image"]}.png')

    return urls
