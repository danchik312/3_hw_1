from aiogram import types
from aiogram.dispatcher.filters import Command
from loader import dp
from config import ADMINS_IDS

@dp.message_handler(Command("admin"), user_id=ADMINS_IDS)
async def show_admin_panel(message: types.Message):
    pass