from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from decouple import config

PROXY_URL = config("PROXY_URL")
TOKEN = config("TOKEN")
ROOT_PATH = config("ROOT_PATH")
DB_PATH = config("DB_PATH")
DB_POOL_MAX_SIZE = int(config("DB_POOL_MAX_SIZE"))

storage = MemoryStorage()
bot = Bot(token=TOKEN, proxy=PROXY_URL)
dispatcher = Dispatcher(bot=bot, storage=storage)