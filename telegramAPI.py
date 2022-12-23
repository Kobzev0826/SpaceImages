import os, telegram, sys
from dotenv import load_dotenv





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
    bot.send_message(text='Test msg!', chat_id=-1001790326720)