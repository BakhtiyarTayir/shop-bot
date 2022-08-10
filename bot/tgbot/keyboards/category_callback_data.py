from aiogram.dispatcher.filters.callback_data import CallbackData

class CategoryCallbackData(CallbackData, prefix="cat"):
    text: str
    cat_id: int