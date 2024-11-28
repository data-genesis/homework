from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import sqlite3
import asyncio
from crud_functions import *

API_TOKEN = ""
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

text = (
    "Product1 | описание 1 | Ценa: 100",
    "Product2 | описание 2 | Ценa: 200",
    "Product3 | описание 3 | Ценa: 300",
    "Product4 | описание 4 | Ценa: 400"
)

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


reply_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_info = types.KeyboardButton(text="Информация")
button_calculate = types.KeyboardButton(text="Рассчитать")
button_buy = types.KeyboardButton(text="Купить")
reg_button = types.KeyboardButton(text="Регистрация")
reply_kb.add(button_calculate, button_info, button_buy, reg_button)

inline_kb = types.InlineKeyboardMarkup(row_width=2)
btn_calories = types.InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories")
btn_formulas = types.InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas")
inline_kb.add(btn_calories, btn_formulas)

initiate_db()
def load_products():
    return get_all_products()


@dp.message_handler(commands=["start"])
async def start_message(message: types.Message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью.", reply_markup=reply_kb)


@dp.message_handler(text=["Информация"])
async def inform(message: types.Message):
    await message.answer("Я помогу вам рассчитать норму калорий и расскажу, как это делается.")


@dp.message_handler(text="Купить")
async def get_buying_list(message: types.Message):
    products = load_products()
    catalog_keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)

    for product in products:
        title, description, price = product[1], product[2], product[3]
        catalog_keyboard.add(InlineKeyboardButton(
            text=f"{title} | {description} | {price}₽",
            callback_data=f"buy_{product[0]}"
        ))

    await message.answer("Выберите продукт: ", reply_markup=catalog_keyboard)


@dp.callback_query_handler(lambda call: call.data.startswith("buy_"))
async def buy_product(call: types.CallbackQuery):
    product_id = int(call.data.split('_')[1])
    products = load_products()
    product = next((p for p in products if p[0] == product_id), None)
    if product:
        title, description, price = product[1], product[2], product[3]
        await call.message.answer(f"Вы успешно приобрели продукт: {title} | {description} | {price}₽")
    else:
        await call.message.answer("Продукт не найден.")


@dp.message_handler(text=["Рассчитать"])
async def main_menu(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=inline_kb)


@dp.callback_query_handler(lambda call: call.data == "formulas")
async def get_formulas(call: types.CallbackQuery):
    formula_text = (" 10 × вес (кг) + 6.25 × рост (см) - 5 × возраст (г) - 161")
    await call.message.answer(formula_text)


@dp.callback_query_handler(lambda call: call.data == "calories")
async def set_age(call: types.CallbackQuery):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    await message.answer("Введите свой рост (см):")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=int(message.text))
    await message.answer("Введите свой вес (кг):")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    age = data["age"]
    growth = data["growth"]
    weight = data["weight"]

    result = 10 * weight + 6.25 * growth - 5 * age + 5
    await message.answer(f"Ваша норма калорий: {result} ккал")
    await state.finish()

@dp.message_handler(text="Регистрация")
async def sing_up(message: types.Message):
    await message.answer("Введите имя пользователя (только латинский алфавит): ")
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    if is_included(message.text) is False:
        await state.update_data(username=(message.text))
        await message.answer("Введите email: ")
        await RegistrationState.email.set()
    else:
        await message.answer("Пользователь существует, введите другое имя")
        await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    await state.update_data(email=(message.text))
    await message.answer("Введите свой возраст: ")
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    await state.update_data(age=(message.text))
    user_data = await state.get_data()
    username = user_data["username"]
    email = user_data["email"]
    age = user_data["age"]
    add_user(username, email, age)
    await message.answer(f"{username}, вы зарегистрированы.")
    await state.finish()



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
