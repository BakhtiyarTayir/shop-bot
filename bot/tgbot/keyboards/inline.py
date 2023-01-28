from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup, InlineKeyboardButton

from tgbot.services.api import get_cats, get_products
from tgbot.keyboards.callback_data_factory import CategoryCallbackFactory, ProductsCallbackFactory


async def menu_cats():
    categories = InlineKeyboardBuilder()
    categories.adjust(1)
    cats = await get_cats()
    for cat_id, cat_name in cats.items():
        categories.add(InlineKeyboardButton(
            text=cat_name,
            callback_data=CategoryCallbackFactory(text=cat_name, cat_id=cat_id).pack())
        )
    categories.adjust(2)
    return categories


async def products_menu_ink(cat_id):
    menu = InlineKeyboardBuilder()
    menu.adjust(1)
    products = await get_products(cat_id)
    for product in products:
        for title, name in product.items():
            menu.add(InlineKeyboardButton(
                text=name,
                callback_data=ProductsCallbackFactory(text=title, product_id=title).pack()
            ))
    menu.adjust(2)
    return menu


async def make_inline_keyboard(cat_id) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    products = await get_products(cat_id)
    for product in products:
        keyboard.row(InlineKeyboardButton(
            text=product['title'],
            callback_data=ProductsCallbackFactory(product_id=product['id'], as_separate=False).pack()
        ))

    return keyboard.as_markup()

#
# def make_replay_keyboard(size: int, bombs: int) -> InlineKeyboardMarkup:
#     keyboard = InlineKeyboardBuilder()
#     keyboard.row(InlineKeyboardButton(
#         text=f"New game ({size}×{size} field, {bombs} bombs)",
#         callback_data=NewGameCallbackFactory(size=size, bombs=bombs, as_separate=True).pack()))
#     keyboard.row(InlineKeyboardButton(text="New game (other)", callback_data="choose_newgame"))
#     return keyboard.as_markup()
