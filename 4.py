##################LIBRARIES ######################
import asyncio
import logging
import os
import random
from dotenv import load_dotenv

##############libs for bot ##################
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

############### new imports ###############
from aiogram.utils.keyboard import ReplyKeyboardBuilder



load_dotenv()
MY_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=MY_TOKEN)


dp = Dispatcher()
logging.basicConfig(level=logging.INFO)
waiting_for_count = {}

@dp.message(Command("numbers"))
async def cmd_numbers(message: Message):
    waiting_for_count[message.from_user.id] = True
    await message.answer("Введите количество кнопок (число):")
@dp.message(F.text)
async def generate_random_buttons(message: Message):
    user_id = message.from_user.id
    if not waiting_for_count.get(user_id):
        await message.answer("Сначала введите команду /numbers")
        return
    try:
        count = int(message.text)
        if count <= 0:
            await message.answer("Число должно быть больше нуля!")
            return
    except ValueError:
        await message.answer("Ошибка! Введите целое число.")
        return
    kb = ReplyKeyboardBuilder()
    for _ in range(count):
        random_num = random.randint(1, 100)
        kb.button(text=str(random_num))
    kb.adjust(4)

    waiting_for_count[user_id] = False
    await message.answer(
        f"Вот ваши кнопки ({count} ps5.):", 
        reply_markup=kb.as_markup(resize_keyboard=True)
    )
async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())
