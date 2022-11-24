from aiogram import executor

from create_bot import dp
from handlers import main_handlers


async def start(_):
    print('Бот запущен')


main_handlers.register(dp)


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True, on_startup=start)
