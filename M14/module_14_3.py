from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

API_TOKEN = ""
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

products = {
    1: [1, 100],
    2: [2, 200],
    3: [3, 300],
    4: [4, 400]
}

text = (f"Product1 | описание {products[1][0]} | Ценa: {products[1][1]}",
        f"Product2 | описание {products[2][0]} | Ценa: {products[2][1]}",
        f"Product3 | описание {products[3][0]} | Ценa: {products[3][1]}",
        f"Product4 | описание {products[4][0]} | Ценa: {products[4][1]}"
        )
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()



reply_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_info = types.KeyboardButton(text="Информация")
button_calculate = types.KeyboardButton(text="Рассчитать")
button_buy = types.KeyboardButton(text="Купить")
reply_kb.add(button_calculate, button_info, button_buy)

catalog_keyboard = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=f"{products[1][0]} Морс ", callback_data="buy_pushare")],
        [InlineKeyboardButton(text=f"{products[2][0]} Морс 2", callback_data="buy_pushare")],
        [InlineKeyboardButton(text=f"{products[3][0]} Зажигалка", callback_data="buy_pushare")],
        [InlineKeyboardButton(text=f"{products[4][0]} Вода", callback_data="buy_pushare")]
    ], resize_keyboard = True
)

inline_kb = types.InlineKeyboardMarkup(row_width=2)
btn_calories = types.InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories")
btn_formulas = types.InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas")
inline_kb.add(btn_calories, btn_formulas)


@dp.message_handler(commands=["start"])
async def start_message(message: types.Message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью.", reply_markup=reply_kb)
@dp.message_handler(text=["Информация"])
async def inform(message: types.Message):
    await message.answer("Я помогу вам рассчитать норму калорий и расскажу, как это делается.")
@dp.message_handler(text="Купить")
async def get_buying_list(message: types.Message):
    with open("mors1.png", "rb") as img1:
        await message.answer_photo(img1, text[0])
    with open("mors2.png", "rb") as img2:
        await message.answer_photo(img2, text[1])
    with open("bic.png", "rb") as img3:
        await message.answer_photo(img3, text[2])
    with open("evian.png", "rb") as img4:
        await message.answer_photo(img4, text[3])
        await message.answer("Выберите продукт: ", reply_markup=catalog_keyboard)

@dp.callback_query_handler(lambda call: call.data == "buy_pushare")
async def buy_pushare(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")

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


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
