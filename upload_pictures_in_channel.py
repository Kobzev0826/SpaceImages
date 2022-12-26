import os, telegram, sys
import time
import random
import telegramAPI
from dotenv import load_dotenv


def get_all_pictures_path_from_dir(dir_path):
    pictures = []
    for root, dirs, files in os.walk(dir_path):
      for file in files:
        if file.endswith(".png") or file.endswith(".jpg"):
          pictures.append(os.path.join(root, file))
    return pictures


if __name__ == '__main__':
    load_dotenv()
    bot = telegram.Bot(token=telegramAPI.read_from_enviroment('TELEGRAM_BOT_TOKEN'))
    pause = int(telegramAPI.read_from_enviroment('PAUSE'))
    chat_id = telegramAPI.read_from_enviroment('CHAT_ID')
    while True:
      pictures = get_all_pictures_path_from_dir({os.getcwd()})
      random.shuffle(pictures)
      while pictures:
        telegramAPI.send_photo(bot, pictures.pop(),chat_id )
        time.sleep(pause)