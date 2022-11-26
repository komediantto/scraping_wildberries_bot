import re
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import scraper.scraper as scraper
import keyboard.main_keyboard as keyboard
from aiogram.dispatcher.filters import Text


class Query(StatesGroup):
    text = State()
    city = State()


async def hello(message: types.Message):
    await message.answer(
        'Выберите город: ',
        parse_mode='HTML', reply_markup=keyboard.choose_city())


async def give_me_data(message: types.Message, state: Query.city):
    await state.update_data(city=message.text)
    await message.answer(
        ('Введите ваш запрос в следующем формате:\n'
         '<b>Артикулы</b>(через запятую, без пробелов) <b>Запрос</b>\n'
         'Пример 1: 17000034 Кувшин\nПример 2: 12334567,13548741 Масло'),
        parse_mode='HTML')
    await state.set_state(Query.text)


async def get_data(message: types.Message, state: Query.text):
    if not re.search(r'(^(?:\d*,)+\d*?|^\d*)[ ].*', message.text):
        await message.answer('Введите запрос согласно инструкции:')
        await state.set_state(Query.text)
    else:
        current_data = await state.get_data()
        search_params = message.text.split(" ", 1)
        query = search_params[1].lower()
        articul = search_params[0].split(',')
        print(articul)
        answers = scraper.find_goods(
            query=query, articul=articul, city=current_data['city'])
        if type(answers) is list:
            for answer in answers:
                await message.answer(answer, parse_mode='HTML')
        else:
            await message.answer(answers, parse_mode='HTML')
        await state.reset_state()
        await hello(message)


def register(dp: Dispatcher):
    dp.register_message_handler(hello, commands=['start'])
    dp.register_message_handler(get_data, state=Query.text)
    dp.register_message_handler(give_me_data,
                                Text(equals=['Калининград',
                                             'Москва', 'Санкт-Петербург']))
