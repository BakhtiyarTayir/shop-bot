from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder 
from tgbot.services.api import get_cats, get_products




async def menu_cats():
    categories = InlineKeyboardBuilder()
    categories.adjust(1)
    cats = await get_cats()
    for cat_id, cat_name in cats.items():
        categories.add(types.InlineKeyboardButton(text=cat_name, callback_data="cat_" + cat_id ))
    categories.adjust(2)
    return categories

async def products_menu(cat_id):
    menu = InlineKeyboardBuilder()
    menu.adjust(1)
    products = await get_products(cat_id)
    for name, id in products.items():
        menu.row(types.InlineKeyboardButton(text=name, callback_data=id))