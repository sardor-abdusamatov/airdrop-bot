##################LIBRARIES ######################
import asyncio
import logging
import os
from dotenv import load_dotenv

##############libs for bot ##################
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

############### new imports ###############
from aiogram.utils.keyboard import InlineKeyboardBuilder

# ------------------Настройка бота--------------------------
load_dotenv()
MY_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=MY_TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)


@dp.message(Command("start"))
async def start(message: Message):
  kb = InlineKeyboardBuilder()
  kb.button(text="Red", callback_data="rred")
  kb.button(text="Green", callback_data="gran")
  kb.button(text="Blue", callback_data="ble")
  kb.adjust(2)
  await message.answer(
      "Click to see the color ",
      reply_markup=kb.as_markup(),
  )

@dp.callback_query(F.data == "rred")
async def ruchka(callback: CallbackQuery):
  await callback.message.answer("🔴Red")
  await callback.answer()


@dp.callback_query(F.data == "gran")
async def granit(callback: CallbackQuery):
  await callback.message.answer("🟢Green")
  await callback.answer()


@dp.callback_query(F.data == "ble")
async def hblue(callback: CallbackQuery):
  await callback.message.answer("🔵Blue")
  await callback.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
