from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from decouple import config

TOKEN = config("TOKEN")
ROOT_PATH = config("ROOT_PATH")
DB_PATH = config("DB_PATH")
DB_POOL_MAX_SIZE = int(config("DB_POOL_MAX_SIZE"))

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot=bot, storage=storage)