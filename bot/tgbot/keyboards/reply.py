from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder 



builder = ReplyKeyboardBuilder()

builder.add(types.KeyboardButton(text="Каталог"))
builder.add(types.KeyboardButton(text="Корзина"))
builder.add(types.KeyboardButton(text="Поиск"))
builder.add(types.KeyboardButton(text="Настройки"))
builder.add(types.KeyboardButton(text="Контакты"))
builder.adjust(2)