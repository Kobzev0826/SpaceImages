import requests
import os
import spacexAPI, nasaAPI
from urllib.parse import urlparse, unquote


def download_image(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.content


def save_image(dir_path, filename, image):
    try:
        os.makedirs(dir_path)
    except FileExistsError:
        pass

    with open(f'{dir_path}/{filename}', 'wb') as file:
        file.write(image)


def download_and_save_image(directory_path, filename, url):
    save_image(directory_path, filename, download_image(url))


def get_filename(url):
    tail = urlparse(os.path.split(url)[-1])
    return (os.path.splitext(unquote(tail.path)))


def save_images(dir_path, links):
    for url in links:
        filename, extension = get_filename(url)
        download_and_save_image(f'{dir_path}', f'{filename}{extension}', url)


def fetch_spacex_last_launch(dir_path):
    save_images(dir_path, spacexAPI.get_imageurls_latest())


def fetch_nasa_pictures(dir_path, num_of_images=5):
    save_images(dir_path, nasaAPI.get_random_images_links(num_of_images))


def fetch_nasa_epic_pictures(dir_path):
    for url in nasaAPI.get_epic_links():
        payload = {
            "api_key": nasaAPI.read_token(),
        }
        response = requests.get(url, params=payload)
        response.raise_for_status()
        image = response.content

        filename, extension = get_filename(url)
        save_image(dir_path, f'{filename}{extension}', image)


# fetch_spacex_last_launch('images_spaceX')
# fetch_nasa_pictures('nasa_pic')
fetch_nasa_epic_pictures('nasa_epic')
