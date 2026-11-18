##################LIBRARIES ######################
import asyncio
import logging
import os
from dotenv import load_dotenv

##############libs for bot ##################
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

############### new imports ###############
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# ------------------Bot Setup--------------------------
load_dotenv()
MY_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=MY_TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

user_numbers = {}


# ------------------Handlers--------------------------
@dp.message(Command("start"))
async def start(message: Message):
  await message.answer("Send two numbers \n Example: 10 2")


@dp.message(F.text == "+")
async def add_numbers(message: Message):
  a, b = user_numbers[message.from_user.id]
  await message.answer(f"{a} + {b} = {a + b}")


@dp.message(F.text == "-")
async def sub_numbers(message: Message):
  a, b = user_numbers[message.from_user.id]
  await message.answer(f"{a} - {b} = {a - b}")


@dp.message(F.text == "*")
async def mul_numbers(message: Message):
  a, b = user_numbers[message.from_user.id]
  await message.answer(f"{a} * {b} = {a * b}")


@dp.message(F.text == "/")
async def div_numbers(message: Message):
  try:
    a, b = user_numbers[message.from_user.id]
    await message.answer(f"{a} / {b} = {a / b}")
  except ZeroDivisionError:
    await message.answer("Cannot divide by zero!")


@dp.message(F.text)
async def get_numbers(message: Message):
  try:
    a, b = map(int, message.text.split())
  except ValueError:
    await message.answer("Error! Send two numbers with space ")
    return

  user_numbers[message.from_user.id] = (a, b)

  kb = ReplyKeyboardBuilder()
  kb.button(text="+")
  kb.button(text="-")
  kb.button(text="*")
  kb.button(text="/")
  kb.adjust(4)

  await message.answer(
      "Choose an operator:", reply_markup=kb.as_markup(resize_keyboard=True)
  )


async def main():
  await dp.start_polling(bot)


if __name__ == "__main__":
  asyncio.run(main())
