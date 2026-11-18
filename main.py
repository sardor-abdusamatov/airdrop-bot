##################LIBRARIES ######################
import os
import asyncio
import logging
import random
from dotenv import load_dotenv
##############libs for bot ##################
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
############### new imports ###############
from aiogram.utils.keyboard import (ReplyKeyboardBuilder, 
                                    InlineKeyboardBuilder)

# ------------------Настройка бота--------------------------
load_dotenv()
MY_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=MY_TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)
# ------------------Хэндлеры--------------------------
@dp.message(Command("start"))
async def start(message: Message):
    kb = ReplyKeyboardBuilder()
    kb.button(text="Start")
    kb.button(text="Done")
    await message.answer("Чтобы пользоваться ботом, подпишитесь на наш канал.", reply_markup=kb.as_markup(
                                                resize_keyboard=True
    ))

@dp.message(F.text == "Start")
async def start_command(message:Message):
    await message.answer(f"Hello {message.from_user.full_name}!")

@dp.message(Command("Subscribe"))
async def Subscribe(message: Message):
    kb = InlineKeyboardBuilder()
    kb.button(text="Subscribe", callback_data="Subscibe")
    await  message.answer("Checking", reply_markup=kb.as_markup())
@dp.message(F.text == "Done")
async def start_command(message:Message):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = a + b
    await message.answer(f"🟢 Subscription verified!")
    await message.answer(f"🔐 Чтобы продолжить, решите пример: {a} + {b} = ? Напишите ответ числом в чат.")
@dp.message(F.text == str(c))
async def verified(message: Message):
    await  message.answer(" Готово, можно пользоваться ботом.Добро пожаловать, 𝕊𝔸ℝ𝔻𝕆ℝ! \n Ваш бесплатный VPN уже готов.\n Подключение займет около минуты.  \n Выберите устройство и получите доступ.")
# --------------------------------------------


# ------------------Запуск бота--------------------------
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())