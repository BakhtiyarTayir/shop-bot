from aiogram.dispatcher.filters.callback_data import CallbackData


class CategoryCallbackFactory(CallbackData, prefix="cat"):
    text: str
    cat_id: int


class ProductsCallbackFactory(CallbackData, prefix="product"):
    product_id: int
