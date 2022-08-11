from aiogram import Router
from aiogram.types import Message, CallbackQuery
from tgbot.keyboards.inline import menu_cats, products_menu_ink
from tgbot.keyboards.category_callback_data import CategoryCallbackData


cats_menu_router = Router()
products_menu = Router()


@cats_menu_router.message(text="Каталог")
async def get_categories(message: Message):
    menu = await menu_cats()
    print(menu)
    await message.answer(
        'Категории',
        reply_markup=menu.as_markup()
        )

@products_menu.callback_query_handler(CategoryCallbackData.filter())
async def get_products(callback: CallbackQuery, callback_data: CategoryCallbackData):
    cat_id = callback_data.cat_id
    print(cat_id)
    menu = await products_menu_ink(cat_id)
    await callback.message.edit_text(
        'Товары',
        reply_markup=menu.as_markup()
        )


