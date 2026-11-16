######################## LIBRARIES ########################
import os
import asyncio
import logging
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import random
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import FSInputFile
################ BOT TOKEN#######################
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
#################### BOT SETTINGS ########################
bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)
####################  HANDLERS  ############################
@dp.message(Command("start"))
async def start(message: Message):
    # Создаем клавиатуру с двумя кнопками
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🎰 Bet"), KeyboardButton(text="💪 Discipline")]
        ],
        resize_keyboard=True,  # Делаем кнопки компактными
        input_field_placeholder="Выберите действие"
    )

    # Отправляем приветствие и прикрепляем клавиатуру
    await message.answer(
        f"HI {message.from_user.full_name}, WELCOME TO THE AIRDROP!",
        reply_markup=keyboard
    )


# Бот будет реагировать И на команду /bet, И на текст с кнопки "🎰 Bet"
@dp.message(Command("bet"))
@dp.message(F.text == "🎰 Bet")
async def bet_command(message: Message):
    a = random.randint(1, 10)
    await message.answer(f"{message.from_user.full_name}, you did bet and won {a} stars")
    rich_sticker_id = "CAACAgIAAxkBAAM8avsl1PY-6L1ZIQxgOt0uDVjlDgEAArBtAAKFz0BIgiAQDEsF5qs9BA"
    await message.answer_sticker(sticker=rich_sticker_id)


# Бот будет реагировать И на команду /discipline, И на текст с кнопки "💪 Discipline"
@dp.message(Command("discipline"))
@dp.message(F.text == "💪 Discipline")
async def discipline_command(message: Message):  # Переименовал функцию, чтобы не было any_action
    await message.answer("yES YEs")
    discipline_id = "CAACAgIAAxkBAANcavsm9wXvkBAOu2xx-vLxeoZp8hcAAr5kAAJHNOFKPK1N-y0HdCA9BA"
    await message.answer_sticker(sticker=discipline_id)


##################### START BOT #################

async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())