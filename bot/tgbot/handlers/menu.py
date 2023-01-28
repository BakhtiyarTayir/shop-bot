from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.fsm.context import FSMContext
from tgbot.keyboards.inline import menu_cats, products_menu_ink, make_inline_keyboard
from tgbot.keyboards.callback_data_factory import CategoryCallbackFactory, ProductsCallbackFactory
from tgbot.services.api import get_products
from tgbot.misc.states import CategoryBack

cats_menu_router = Router()
products_menu = Router()
single_product = Router()


@cats_menu_router.message(text="Каталог")
async def get_categories(message: Message, state: FSMContext):
    menu = await menu_cats()
    print(menu)
    await message.answer(
        'Категории',
        reply_markup=menu.as_markup()
    )
    await state.set_state(CategoryBack.category_back)


@products_menu.callback_query(CategoryBack.category_back, CategoryCallbackFactory.filter())
async def get_products(callback: CallbackQuery, callback_data: CategoryCallbackFactory):
    cat_id = callback_data.cat_id
    print(cat_id)
    menu = await make_inline_keyboard(cat_id)
    await callback.message.edit_text(
        'Товары',
        reply_markup=menu
    )


@single_product.callback_query(ProductsCallbackFactory.filter())
async def get_product(callback: CallbackQuery, callback_data: ProductsCallbackFactory):
    print(callback_data)
    await callback.message.answer(
        'Product',

    )
