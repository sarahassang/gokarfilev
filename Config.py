import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "HunerThon")
    CHANNEL = os.environ.get("CHANNEL", "HunerThon")
    START_IMG = os.environ.get("START_IMG", "https://graph.org/file/3ae6f6eb50b6b28bb2fbc.jpg")
    CMD_IMG = os.environ.get("CMD_IMG","https://graph.org/file/3ae6f6eb50b6b28bb2fbc.jpg")
    OWNER_ID = os.environ.get("OWNER_ID", "")

