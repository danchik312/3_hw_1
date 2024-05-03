from aiogram import Bot, Dispatcher
from config import BOT_TOKEN

if BOT_TOKEN is None:
    raise ValueError("BOT_TOKEN is not specified in the .env file")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()