import os, telegram, sys
import time
import random

from dotenv import load_dotenv





def read_from_enviroment(name):
  try:
    load_dotenv()
    token = os.environ[f"{name}"]
  except:
    try:
      token = os.environ[f"{name}"]
    except KeyError as e:
      print(f"Error: {e} \n no token in system environment")
      sys.exit()
  return token


def send_photo(bot,photo_path):
    bot.send_photo(chat_id=get_chat_id(), photo=open(f'{photo_path}', 'rb'))


def get_chat_id():
  bot = telegram.Bot(token=read_from_enviroment('TELEGRAM_BOT_TOKEN'))
  updates = bot.get_updates()
  ch_usrname = read_from_enviroment('CH_USERNAME')
  for update in updates:
    if update['my_chat_member']:
      if update['my_chat_member']['chat']['username'] == ch_usrname:
        return update['my_chat_member']['chat']['id']
      else:
        print(f"I don't see a channel with username={ch_usrname}")
        sys.exit()


if __name__ == '__main__':
    pass