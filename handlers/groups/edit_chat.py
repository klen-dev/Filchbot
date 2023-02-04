import io


from aiogram import executor
from aiogram.dispatcher import filters
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
from loader import dp, bot
from aiogram.utils.exceptions import BadRequest
from filters import IsGroup, IsAdmin

SUPERUSERS=['5828291838','5030589586']

@dp.message_handler(IsGroup(), Command("bayroq", prefixes="!"),IsAdmin())
async def set_bayroq(message:types.Message):
    source_message = message.reply_to_message
    photo = source_message.photo[-1]
    photo = await photo.download(destination=io.BytesIO())
    input_file = types.InputFile(photo)
    if message.reply_to_message.from_user.id==5828291838 or message.reply_to_message.from_user.id==5030589586:
        await message.chat.set_photo(photo=input_file)
        await message.answer(f'<b>🔥 "➒¾ New Hogwarts 🏰"ga g`olib fakultet bayrog`i muvaffaqiyatli ilindi! \n'
                        f'Hogwarts rahbari - {message.from_user.mention}</b>')



