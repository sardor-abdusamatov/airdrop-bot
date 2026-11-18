##################LIBRARIES ######################
import asyncio
import logging
import os
import random
from dotenv import load_dotenv

##############libs for bot ##################
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

############### new imports ###############
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

# ------------------Настройка бота--------------------------
load_dotenv()
MY_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=MY_TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)
user_answers = {}
# ------------------Хэндлеры--------------------------
@dp.message(Command("start"))
async def start(message: Message):
  kb = InlineKeyboardBuilder()
  kb.button(text="Start", callback_data="btn_start")
  kb.button(text="Done", callback_data="btn_done")
  await message.answer(
      "Чтобы пользоваться ботом, подпишитесь на наш канал.",
      reply_markup=kb.as_markup(),
  )


@dp.callback_query(F.data == "btn_start")
async def start_command(callback: CallbackQuery):
  await callback.message.answer(f"Hello {callback.from_user.full_name}!")
  await callback.answer()


@dp.message(Command("Subscribe"))
async def Subscribe(message: Message):
  kb = InlineKeyboardBuilder()
  kb.button(text="Subscribe", callback_data="Subscibe")
  await message.answer("Checking", reply_markup=kb.as_markup())


@dp.callback_query(F.data == "btn_done")
async def done_command(callback: CallbackQuery):
  a = random.randint(1, 10)
  b = random.randint(1, 10)
  user_answers[callback.from_user.id] = str(a + b)

  await callback.message.answer("🟢 Subscription verified!")
  await callback.message.answer(
      f"🔐 Чтобы продолжить, решите пример: {a} + {b} = ? Напишите ответ числом"
      " в чат."
  )
  await callback.answer()


@dp.message(
    lambda message: message.from_user.id in user_answers
    and message.text == user_answers[message.from_user.id]
)
async def verified(message: Message):
  del user_answers[message.from_user.id]

  kb = InlineKeyboardBuilder()
  kb.button(text="iOS", callback_data="device_ios")
  kb.button(text="Android", callback_data="device_android")
  kb.button(text="Windows / macOS", callback_data="device_pc")
  kb.adjust(2)

  await message.answer(
      "Готово, можно пользоваться ботом. Добро пожаловать, 𝕊𝔸ℝ𝔻𝕆ℝ!\n"
      "Ваш бесплатный VPN уже готов.\n"
      "Подключение займет около минуты.\n"
      "Выберите устройство и получите доступ.",
      reply_markup=kb.as_markup(),
  )


@dp.callback_query(F.data.startswith("device_"))
async def device_selected(callback: CallbackQuery):
  vpn_key = "https://us-east.bltscdn.com/v2/0c00e94b-4ebb-477a-bb5b-b7ffefaee78d"
  await callback.message.answer(
      "1. Скачайте приложение Happ.\n"
      f"2. Скопируйте ключ: <code>{vpn_key}</code>\n"
      "3. В Happ нажмите «+» -> «Импортировать из буфера» и запустите VPN.",
      parse_mode="HTML",
  )
  await callback.answer()

# --------------------------------------------
# ------------------Запуск бота--------------------------

async def main():
  await dp.start_polling(bot)
if __name__ == "__main__":
  asyncio.run(main())
