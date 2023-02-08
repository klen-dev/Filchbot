import io


from aiogram import executor
from aiogram.dispatcher import filters
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
from loader import dp, bot
from aiogram.utils.exceptions import BadRequest
from filters import IsGroup, IsAdmin
# from aiogram.dispatcher.filters import Command
from pyrogram.types import ChatPermissions


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


@dp.message_handler(IsGroup(), Command("qtime", prefixes="!/"), IsAdmin())
async def mutegroup(message: types.Message):
    stikerid='CAACAgIAAxkBAAIHBmPjW0GqYvmEpXiKRCEa-bXV9fGHAAIRGwACwTiZS2lcQQaGpweELgQ'
    stiker2='CAACAgIAAxkBAAIHCmPjY8_rUkA4YYWWAAFf1cW_jVwBLQACYSAAAlEhkUsi6RVRCOipny4E'
    # await message.chat.id(ChatPermissions(can_send_media_messages=False))
    await message.chat.set_permissions(
        # message.chat.id,
        ChatPermissions(
        can_send_messages=False
        )
    )
    await message.answer_sticker(stikerid)
    await message.answer_sticker(stiker2)

@dp.message_handler(IsGroup(), Command("mtime", prefixes="!/"), IsAdmin())
async def mutegroup(message: types.Message):
    stikerid='CAACAgIAAxkBAAIHBmPjW0GqYvmEpXiKRCEa-bXV9fGHAAIRGwACwTiZS2lcQQaGpweELgQ'
    await message.chat.set_permissions(
        # message.chat.id,
        ChatPermissions(
        can_send_messages=False
        )
    )
    await message.answer_sticker(stikerid)
    await message.answer_sticker('CAACAgIAAxkBAAIHDGPjagvgxcNNqNBGXAQZ-eOqFdy_AALeGwACs6OQS1KyVn70IA-ALgQ')

@dp.message_handler(IsGroup(), Command("ugroup", prefixes="!/"), IsAdmin())
async def unmutegroup(message: types.Message):
    await message.chat.set_permissions(
        # message.chat.id,
        ChatPermissions(
        can_send_messages=True,
        can_invite_users=True
        )
    )
    await message.answer_sticker('CAACAgIAAxkBAAIHDmPja1PBviKJs1lqN3Uz2S4xxf83AALTHQACTnKQS8s0b_eUt_kpLgQ')
    
@dp.message_handler(IsGroup(), Command("mgroup", prefixes="!/"), IsAdmin())
async def unmutegroup(message: types.Message):
    await message.chat.set_permissions(
        ChatPermissions(
        can_send_messages=False,
        can_invite_users=True
        )
    )
    await message.answer_sticker('CAACAgIAAxkBAAIHBmPjW0GqYvmEpXiKRCEa-bXV9fGHAAIRGwACwTiZS2lcQQaGpweELgQ')