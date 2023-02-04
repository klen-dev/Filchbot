import asyncio
import datetime
import re
import aiogram

from loader import dp, bot
from aiogram import types, Dispatcher
from aiogram.utils.exceptions import BadRequest
from filters import IsGroup, IsAdmin
from aiogram.dispatcher.filters import Command

ADMIN1=5828291838
ADMIN2=5030589586

@dp.message_handler(IsGroup(), Command("mute", prefixes="!"), IsAdmin())
async def mute(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id
    command_parse = re.compile(r"(!mute) ?(\d+)? ?([\w+\D]+)?")
    parsed = command_parse.match(message.text)
    time = parsed.group(2)
    comment = parsed.group(3)
    if not time: 
        time = 24

    time = int(time)

    until_date = datetime.datetime.now() + datetime.timedelta(hours=time)    

    try:
        await message.chat.restrict(user_id=member_id, can_send_messages=False, until_date=until_date)
        await message.reply_to_message.delete()
    except aiogram.utils.exceptions.BadRequest as err:
        await message.delete()
        return

    answer_message_mute = await message.answer(f"<b>🚫 Hogwarts a'zosi {message.reply_to_message.from_user.mention} {time} soat yoza olmaslik rejimiga tushirildi!\n"
    f"Sabab: <i>{comment}</i></b>")
    await message.delete()
    await dp.bot.send_message(ADMIN1, f"❗️<b>{message.reply_to_message.from_user.mention} mute holatiga tushirildi!\n"
                              f"👨‍💻 Admin: {message.from_user.mention}\n"
                              f"📝 Sababi: {comment}\n"
                              f"⏰ Vaqt: {time} soat</b>")  
    await dp.bot.send_message(ADMIN2, f"❗️<b>{message.reply_to_message.from_user.mention} mute holatiga tushirildi!\n"
                              f"👨‍💻 Admin: {message.from_user.mention}\n"
                              f"📝 Sababi: {comment}\n"
                              f"⏰ Vaqt: {time} soat</b>")       
    await asyncio.sleep(120)
    await answer_message_mute.delete()

@dp.message_handler(IsGroup(), IsAdmin(), Command("unmute", prefixes="!"))
async def unmute(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id


    user_allowed =  types.ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_other_messages=True,
        can_invite_users=True,
        can_add_web_page_previews=True,
        can_change_info=True,
        can_pin_messages=True,
        can_send_polls=True,
    )

    reply_message_unmute = await message.answer(f"<b>✅ Hogwarts a'zosi {message.reply_to_message.from_user.mention} guruhda yozishi mumkin!</b>")    
    await message.chat.restrict(user_id=member_id, permissions=user_allowed, until_date=0)
    await message.delete()
    await asyncio.sleep(60)
    await reply_message_unmute.delete()
        
        
@dp.message_handler(IsGroup(), IsAdmin(), Command("ban", prefixes="!"))
async def ban(message: types.Message):
    member=message.reply_to_message.from_user
    member_id=member.id
    await message.chat.kick(user_id=member_id)
    haydaldi_message = await message.answer(f"<b>❗️Hogwartsdan {message.reply_to_message.from_user.mention} haydaldi!</b>")
    await dp.bot.send_message(ADMIN1, f"<b>❗️Hogwartsdan {message.reply_to_message.from_user.mention} haydaldi!"
                            f"👨‍💻 Admin: {message.from_user.mention}</b>")  
    await dp.bot.send_message(ADMIN2, f"<b>❗️Hogwartsdan {message.reply_to_message.from_user.mention} haydaldi!"
                            f"👨‍💻 Admin: {message.from_user.mention}</b>")              
    await asyncio.sleep(60)
    await message.delete()
    await haydaldi_message.delete()