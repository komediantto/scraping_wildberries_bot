from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def choose_city():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton('Калининград')
    b2 = KeyboardButton('Москва')
    b3 = KeyboardButton('Санкт-Петербург')
    keyboard.row(b1, b2)
    keyboard.row(b3)
    return keyboard
