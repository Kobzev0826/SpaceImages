import requests, os
from urllib.parse import urlparse, unquote


def download_image(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.content


def get_filename_from_url(url):
    tail = urlparse(os.path.split(url)[-1])
    return os.path.splitext(unquote(tail.path))


def save_images(dir_path, links):
    for url in links:
        filename, extension = get_filename_from_url(url)
        save_image(f'{dir_path}', f'{filename}{extension}', download_image(url))


def save_image(dir_path, filename, image):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    with open(f'{dir_path}/{filename}', 'wb') as file:
        file.write(image)
