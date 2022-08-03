from aiogram import Router
from aiogram.types import Message
from tgbot.keyboards.inline import menu_cats
cats_menu_router = Router()


@cats_menu_router.message(text="Каталог")
async def get_categories(message: Message):
    menu = await menu_cats()
    await message.answer(
        'Категории',
        reply_markup=menu.as_markup()
        )