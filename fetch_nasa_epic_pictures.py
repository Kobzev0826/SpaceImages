import argparse, requests
import nasaAPI, download_images


if __name__=='__main__':
    parser = argparse.ArgumentParser(description="download images from spacexdata.com")
    parser.add_argument(
        '-dir',
        '--dir_path',
        default='nasa_epic_pictures',
        help='directory where pictures will be saved, default="nasa_epic_pictures"'
    )
    app_args = parser.parse_args()

    for url in nasaAPI.get_epic_links():
        payload = {
            "api_key": nasaAPI.read_token(),
        }
        response = requests.get(url, params=payload)
        response.raise_for_status()
        image = response.content

        filename, extension = download_images.get_filename(url)
        download_images.save_image(app_args.dir_path, f'{filename}{extension}', image)