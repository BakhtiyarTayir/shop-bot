
from aiogram import types
from aiogram import Router
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from tgbot.keyboards.reply import builder

from tgbot.filters.admin import AdminFilter

admin_router = Router()
admin_router.message.filter(AdminFilter())


@admin_router.message(commands=["start"], state="*")
async def admin_start(message: Message):
    await message.answer(
        "Выберите число:",
        reply_markup=builder.as_markup(resize_keyboard=True),
        )
