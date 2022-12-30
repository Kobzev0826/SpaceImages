import sys, argparse
import spacexAPI
import download_images


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="download images from spacexdata.com")
    parser.add_argument('-id', help='id of launch if None download last launch', default='latest')
    parser.add_argument('--dir_path',
                        help='directory where pictures will be saved, default="spacex_pictures"',
                        default="spacex_pictures")
    app_args = parser.parse_args()

    urls = spacexAPI.get_imageurls_latest(f'https://api.spacexdata.com/v5/launches/{app_args.id}')

    if not urls:
        print('Unfortunately, there are no photos of the last run.')
        sys.exit()

    download_images.save_images(app_args.dir_path, urls)
