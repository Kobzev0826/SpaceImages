import argparse, requests
import nasaAPI, download_images
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()
    parser = argparse.ArgumentParser(description="download images from spacexdata.com")
    parser.add_argument(
        '-dir',
        '--dir_path',
        default='nasa_epic_pictures',
        help='directory where pictures will be saved, default="nasa_epic_pictures"'
    )
    app_args = parser.parse_args()
    token = nasaAPI.read_token()
    for url in nasaAPI.get_epic_links(token):
        payload = {
            "api_key": token,
        }
        image = download_images.download_image(url,params=payload)

        filename, extension = download_images.get_filename_from_url(url)
        download_images.save_image(app_args.dir_path, f'{filename}{extension}', image)
