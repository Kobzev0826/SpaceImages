import sys, argparse
import spacexAPI
import download_images

parser = argparse.ArgumentParser(description="download images from spacexdata.com")
parser.add_argument('-id',help='id of launch if None download last launch')
parser.add_argument('-dir','--dir_path',help='directory where pictures will be saved, default="spacex_pictures"')
app_args = parser.parse_args()

if id:
  urls = spacexAPI.get_imageurls_latest(f'https://api.spacexdata.com/v5/launches/{app_args.id}')
else:
  urls = spacexAPI.get_imageurls_latest('https://api.spacexdata.com/v5/launches/latest')
if len(urls) == 0:
  print('Unfortunately, there are no photos of the last run.')
  sys.exit()

dir = app_args.dir_path if app_args.dir_path else 'spacex_pictures'

download_images.save_images(dir,urls)