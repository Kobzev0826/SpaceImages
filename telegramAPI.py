import os, telegram, sys
import argparse
from dotenv import load_dotenv


def read_from_enviroment(name):
    try:
        token = os.environ[f"{name}"]
    except KeyError as e:
        print(f"Error: {e} \n no token in system environment")
        sys.exit()
    return token


def send_photo(bot, photo_path):
    with open(f'{photo_path}', 'rb') as photo:
        bot.send_photo(chat_id=get_chat_id(), photo=photo)


def get_chat_id():
    return read_from_enviroment('CHAT_ID')


if __name__ == '__main__':
    load_dotenv()
    parser = argparse.ArgumentParser(description="upload images ")
    parser.add_argument('--img_path', help='path to images')
    app_args = parser.parse_args()
    bot = telegram.Bot(token=read_from_enviroment('TELEGRAM_BOT_TOKEN'))
    send_photo(bot, app_args.img_path)

