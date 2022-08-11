from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder 


from tgbot.services.api import get_cats, get_products
from tgbot.keyboards.category_callback_data import CategoryCallbackData


async def menu_cats():
    categories = InlineKeyboardBuilder()
    categories.adjust(1)
    cats = await get_cats()
    for id, cat_name in cats.items():
        categories.add(types.InlineKeyboardButton(text=cat_name, callback_data=CategoryCallbackData(text=cat_name, cat_id=id).pack()))
    categories.adjust(2)
    return categories

async def products_menu_ink(cat_id):
    menu = InlineKeyboardBuilder()
    menu.adjust(1)
    products = await get_products(cat_id)
    for product in products:
        for title, name in product.items():
            print(title)
            menu.add(types.InlineKeyboardButton(text=name, callback_data="title"))
    menu.adjust(2)
    return menu