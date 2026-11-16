######################## LIBRARIES ########################
import os
import asyncio
import logging

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
    await message.answer(f"HI {message.from_user.full_name}, ENTER NAME")


@dp.message(F.text)
async def any_action(message: Message):
    request_message = message.text.upper()
    await message.answer(f"UPPER CASE : {request_message}")


##################### START BOT #################

async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())