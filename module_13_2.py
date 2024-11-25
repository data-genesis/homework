from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

API_TOKEN = ""
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(lambda message: not message.text.startswith('/'))
async def all_message(message: types.Message):
    print("Введите команду /start, чтобы начать общение.")

@dp.message_handler(commands=["start"])
async def start_message(message: types.Message):
    print("Привет! Я бот помогающий твоему здоровью.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
