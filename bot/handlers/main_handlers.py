from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import scraper.scraper as scraper

class Query(StatesGroup):
    text = State()


async def hello(message: types.Message, state: FSMContext):
    await message.answer(
        'Введите ваш запрос в следующем формате:\n<b>Артикулы</b>(через запятую, без пробелов) <b>Запрос</b>', parse_mode='HTML')
    await state.set_state(Query.text)


async def get_data(message: types.Message, state: Query.text):
    search_params = message.text.split(" ", 1)
    query = search_params[1].lower()
    print(query)
    articul = search_params[0].split(',')
    print(articul)
    answers = scraper.find_goods(query=query, articul=articul)
    for answer in answers:
        await message.answer(answer)


def register(dp: Dispatcher):
    dp.register_message_handler(hello, commands=['start'])
    dp.register_message_handler(get_data, state=Query.text)
