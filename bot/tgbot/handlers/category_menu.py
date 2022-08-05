from aiogram import Router
from aiogram.types import Message, CallbackQuery
from tgbot.keyboards.inline import menu_cats, products_menu
cats_menu_router = Router()
products_menu = Router()


@cats_menu_router.message(text="Каталог")
async def get_categories(message: Message):
    menu = await menu_cats()
    await message.answer(
        'Категории',
        reply_markup=menu.as_markup()
        )

@products_menu.callback_query_handler(text="1")
async def get_products(callback: CallbackQuery):
    menu = await products_menu(callback.data)
    await callback.answer(
        'Продукты',
        reply_markup=menu.as_markup()
    )
