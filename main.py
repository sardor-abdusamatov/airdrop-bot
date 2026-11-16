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
    await message.answer(f"HI , ENTER NAME")

@dp.message(Command("luck"))
async def start(message: Message):

    luk = random.randint(1,12)
    if luk == 3 or luk == 9 or luk == 12:
        await message.answer(f"You're lucky ")

# @dp.message(F.text)
# async def any_action(message: Message):
#     request_message = message.text
#     await message.answer(f"Your name: {request_message}")

##################### START BOT #################

async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())





