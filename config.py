import os

class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7080988530:AAHt9i0VubFNcY1ndUUZ3NIGsVIUCzlPiSo")
      API_ID = int(os.environ.get("APP_ID", 15964059))
      API_HASH = os.environ.get("API_HASH", "786fd04eca38875885d9427894796c5c")
      CHANNEL = list(x for x in os.environ.get("CHANNEL_ID", "-1002130738193:-1002013915316").replace("\n", " ").split(' '))
