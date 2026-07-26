import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command

TOKEN = "8698371498:AAEkBTr2yn-D0Dd3H3SgIUeIDf9bnSWQZyU"

bot = Bot(token=TOKEN)
dp = Dispatcher()

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🥗 Записаться на консультацию"),
            KeyboardButton(text="💳 Купить программу")
        ],
        [
            KeyboardButton(text="👩 О специалисте"),
            KeyboardButton(text="💬 Связаться с нутрициологом")
        ]
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Привет! 👋\n\n"
        "Я помощник нутрициолога 🥗\n"
        "Выберите действие:",
        reply_markup=menu
    )

@dp.message()
async def buttons(message: Message):
    if message.text == "🥗 Записаться на консультацию":
        await message.answer("Отлично! Напишите ваше имя.")

    elif message.text == "💳 Купить программу":
        await message.answer("Здесь будут программы питания.")

    elif message.text == "👩 О специалисте":
        await message.answer("Здесь будет информация о специалисте.")

    elif message.text == "💬 Связаться с нутрициологом":
        await message.answer("Напишите свой вопрос, и специалист ответит вам.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
