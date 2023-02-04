from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp

from filters import IsGroup, IsAdmin
from aiogram.dispatcher.filters import Command

@dp.message_handler(IsGroup(), Command("fakultet", prefixes="!"), IsAdmin())
async def bot_start(message: types.Message):
    await message.reply_to_message.reply(f"<b>❗️Fakultet olish uchun @hpuz_qalpoq_bot ga murojaat qiling!</b>")
    await message.delete()
