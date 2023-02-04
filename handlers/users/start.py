from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters import IsPrivate
from loader import dp


@dp.message_handler(IsPrivate(), CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")

@dp.message_handler(IsPrivate(), commands='admins')
async def bot_admins(message: types.Message):
    await message.answer(f"Adminlar: @klen_uz va @H_Grenger")    
