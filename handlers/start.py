from aiogram import types
from aiogram.dispatcher.filters import Command
from loader import dp
from database import Database

db = Database()

@dp.message_handler(Command("start"))
async def start_command(message: types.Message):
    db.add_user(message.from_user.id, message.from_user.username)
    await message.answer("Привет! Ты успешно зарегистрирован.")
