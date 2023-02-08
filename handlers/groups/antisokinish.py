import asyncio
import datetime
import aiogram

from loader import dp, bot
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from filters import IsGroup
from aiogram.utils.exceptions import BadRequest

ADMIN=5828291838
sokinishlar = ['jalab','zaybal','chuchoq','tashshoq','joulup', 'jalla', 'seks', 'foxisha', 'dalbayob', 'sikaman', 'qotoq', 'tashoq', 'tashaq', 'dalbayob',
               'qotoq','gandon','гандон', 'qutoq','жалаб','жоулуп','жалла',   'секс', 'фохиша', 'далбаёб', 'сикаман', 'қотоқ', 'ташоқ', 'ташақ', 'далбаёб',
               'қотоқ', 'қутоқ','зайбал','заебал', 'yban','хуйет','🏳️‍🌈','d.n.x', 'p.n.x', '@dnx', '@pnx']
sokinishlar2 = ['qutoqqa','amingga','kotingga','gay', 'nx','gey','xuyyet', 'xuet','kt','kot', 'kut','dlb','om','am', 'jlb', 'gone done', 'joul up', ' one nine sky','dnx', 'pnx','sky','кт','кот', 'кут','длб','ом','ам', 'жлб', 'гоне доне', 'жоул уп', ' оне нине скй','днх', 'пнх','скй']

for i in sokinishlar:
    @dp.message_handler(IsGroup(), Text(equals=sokinishlar2, ignore_case=True))
    @dp.message_handler(IsGroup(), Text(contains=i,ignore_case=True))
    async def sokinish(message: types.Message):
        await message.reply_to_message.delete()
        time = 2
        until_date = datetime.datetime.now() + datetime.timedelta(hours=time)   
        await message.delete()
        try:
            await message.chat.restrict(user_id=message.from_user.id, can_send_messages=False, until_date=until_date)
            sokinmang_message = await message.answer(f"❗️<b>{message.from_user.mention} vaqtincha mute holatiga tushdingiz!\n</b>"
                                                f"<b>Sabab: <i>Taqiqlangan so'z ishlatgani uchun</i></b>")
            await dp.bot.send_message(ADMIN, f"{message.from_user.mention} guruhda so'kindi! \nSo'zlar: {message.text}")
            # await asyncio.sleep(15)
            # await sokinmang_message.delete()
        except aiogram.utils.exceptions.BadRequest as err:
            sokinmang_message = await message.answer(f"❗️<b>Hurmatli {message.from_user.mention} tilingizga ehtiyot bo'ling!</b>")
            await dp.bot.send_message(ADMIN, f"❗️<b>{message.from_user.mention} guruhda so'kindi! \nSo'zlar: {message.text}</b>")
            await asyncio.sleep(120)
            await sokinmang_message.delete()
            return

    