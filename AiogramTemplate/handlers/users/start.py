from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart,CommandHelp

from loader import dp
BLACKLIST=[]

@dp.message_handler(chat_id=BLACKLIST,text='/start')
async def bot_start(message:types.Message):
    text =f"Salom,{message.from_user.full_name}!Siz bloklangansiz"
    await message.answer(text)

# async def bot_start(message: types.Message):
#     await message.answer(f"Salom, {message.from_user.full_name}!")

@dp.message_handler(CommandStart(deep_link="wmc_music_uz"))
async def bot_start(message: types.Message):
    args=message.get_args()
    text = f"Salom,{message.from_user.full_name}!"
    text+=f"sizni {args} taklif qildi"
    await message.answer(text)

@dp.message_handler(CommandHelp())
async def help(msg: types.Message):
    text=f"Bu bot filter uchun yaratilgan"
    await (msg.answer(text))
