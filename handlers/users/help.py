from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from filters import IsGroup, IsAdmin
from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("<b>Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam",
            "!mute - Mute berish",
            "!unmute - Mutedan chiqarish",
            "!bayroq - Bayroq o'rnatish",
            "!mtime - Guruhni yopaman va mafia haqida ogohlantiraman",
            "!qtime - Guruhni yopaman va quiz haqida ogohlantiraman",
            "!oguruh - Guruhni ochaman va bu haqida ogohlantiraman",
            "!fakultet - kim fakultet so'rasa, o'shanga reply qilib yozing"
            "So'kinganlarga o'zim 2 soat mute beraman</b>")
    
    await message.answer("\n".join(text))
