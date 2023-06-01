"""
Модуль объявления фильтров, для настройки обработки сообщений пользователей
"""


import telebot
from telebot import asyncio_filters
from telebot.types import Message

from database import crud


class IsAdmin(telebot.asyncio_filters.SimpleCustomFilter):
    key = 'is_admin'

    @staticmethod
    async def check(message: Message):
        return crud.is_admin(message.from_user.id)
