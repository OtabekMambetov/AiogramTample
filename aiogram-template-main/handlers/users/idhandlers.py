from aiogram import  types
from aiogram.dispatcher import filters

from loader import dp

SUPERUSER = [5350787289]
BLACKLIST = [6743450983]

@dp.message_handler(chat_id=SUPERUSER, text='secret')
async  def id_filter(msg: types.Message):
    await  msg.answer('Xush kelibsiz, SuperUser')

@dp.message_handler(chat_id=BLACKLIST, text='start')
async def id_filter(msg: types.Message):
    await msg.answer('Siz bloqlangansiz, Siz bu botdan foydalana olmaysiz')
