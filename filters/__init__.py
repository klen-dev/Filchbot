from aiogram import Dispatcher

from loader import dp
# from .is_admin import AdminFilter
from .adminFilter import IsAdmin
from .groupfilter import IsGroup
from .privatechat import IsPrivate

if __name__ == "filters":
    dp.filters_factory.bind(IsAdmin)
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsPrivate)
    pass
