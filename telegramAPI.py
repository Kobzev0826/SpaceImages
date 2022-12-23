import os, telegram, sys
from dotenv import load_dotenv


CHAT_ID = -1001790326720


def read_token():
  try:
    load_dotenv()
    token = os.environ["TELEGRAM_BOT_TOKEN"]
  except:
    try:
      token = os.environ["TELEGRAM_BOT_TOKEN"]
    except KeyError as e:
      print(f"Error: {e} \n no token in system environment")
      sys.exit()
  return token


if __name__ == '__main__':
    bot = telegram.Bot(token=read_token())
    # bot.send_message(text='Test msg!', chat_id=CHAT_ID)
    bot.send_photo(chat_id = CHAT_ID, photo = open('nasa_epic/epic_1b_20221221001752.png','rb'))