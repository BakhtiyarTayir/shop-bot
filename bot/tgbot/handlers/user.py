from aiogram import Router
from aiogram.types import Message
from tgbot.keyboards.reply import builder
from tgbot.keyboards.inline import menu_cats
user_router = Router()


@user_router.message(commands=["start"])
async def user_start(message: Message):
    await message.answer(
        f"Привет {message.from_user.first_name}",
        reply_markup=builder.as_markup(resize_keyboard=True),
        )

