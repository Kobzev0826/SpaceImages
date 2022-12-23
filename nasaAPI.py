import requests
import sys, os
from dotenv import load_dotenv


def read_token():
  try:
    load_dotenv()
    token = os.environ["NASA_API"]
  except:
    try:
      token = os.environ["NASA_API"]
    except KeyError as e:
      print(f"Error: {e} \n no token in system environment")
      sys.exit()
  return token


def get_random_images_links(number_of_links):

  payload = {"api_key": read_token(), "count": number_of_links}
  url = "https://api.nasa.gov/planetary/apod"
  response = requests.get(url, params=payload)
  response.raise_for_status()
  data = response.json()
  links = []
  for item in data:
    links.append(item['url'])
  return links


def get_epic_links():
  url = 'https://api.nasa.gov/EPIC/api/natural'
  payload = {
    "api_key": read_token(),
  }
  response = requests.get(url, params=payload)
  response.raise_for_status()
  # print(response.url)
  data = response.json()
  urls = []
  for item in data:
    # print(item)
    # print(f'image={item["image"]}  data={item["date"]}')
    date_time = item["date"].split()[0].split('-')
    dat = "/".join(date_time)
    cur_url = 'https://api.nasa.gov/EPIC/archive/natural/' + dat
    urls.append(f'{cur_url}/png/{item["image"]}.png')
  # print(urls)
  return urls


