import argparse
import nasaAPI, download_images
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()
    parser = argparse.ArgumentParser(description="download images from spacexdata.com")

    parser.add_argument(
        '-noi',
        '--num_of_images',
        type=int,
        default=1,
        help='how many pictures do you want download, default =1'
    )
    parser.add_argument(
        '-dir',
        '--dir_path',
        default='nasa_apod_pictures',
        help='directory where pictures will be saved, default="nasa_apod_pictures"'
    )

    app_args = parser.parse_args()

    download_images.save_images(app_args.dir_path, nasaAPI.get_random_images_links(app_args.num_of_images))
