from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.db.storage import DatabaseManager

from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage) # объект диспетчера для обработки входящих сообщений и запросов
db = DatabaseManager('data/database.db') # объект менеджера баз данных