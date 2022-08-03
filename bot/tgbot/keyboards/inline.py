from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder 
from tgbot.services.api import get_cats


async def menu_cats():
    categories = InlineKeyboardBuilder()
    categories.adjust(1)
    cats = await get_cats()
    for cat_id, cat_name in cats.items():
        categories.row(types.InlineKeyboardButton(text=cat_name, callback_data=cat_id ))
    return categories
