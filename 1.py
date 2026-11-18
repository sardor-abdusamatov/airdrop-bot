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


# ------------------Хэндлеры--------------------------
@dp.message(Command("start"))
async def start(message: Message):
  kb = InlineKeyboardBuilder()
  kb.button(text="Привет", callback_data="btn_hello")
  kb.button(text="Пока", callback_data="btn_bye")
  kb.button(text="Как дела?", callback_data="btn_how_are_you")
  kb.adjust(2)

  await message.answer(
      "Выберите действие",
      reply_markup=kb.as_markup(),
  )


@dp.callback_query(F.data == "btn_hello")
async def hello_command(callback: CallbackQuery):
  await callback.message.answer(f"Привет, {callback.from_user.full_name}!")
  await callback.answer()


@dp.callback_query(F.data == "btn_bye")
async def bye_command(callback: CallbackQuery):
  await callback.message.answer("Пока!")
  await callback.answer()


@dp.callback_query(F.data == "btn_how_are_you")
async def how_are_you_command(callback: CallbackQuery):
  await callback.message.answer("BTW ")
  await callback.answer()


# --------------------------------------------
# ------------------Запуск бота--------------------------


async def main():
  await dp.start_polling(bot)


if __name__ == "__main__":
  asyncio.run(main())
