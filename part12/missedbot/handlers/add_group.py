from telebot.asyncio_handler_backends import StatesGroup, State
from telebot.types import Message

from database import crud
from missedbot import bot


class GroupStates(StatesGroup):
    INPUT_NAME = State()


@bot.message_handler(is_admin=False, commands=["addgroup"])
async def handle_no_add_group(message: Message):
    await bot.send_message(message.chat.id, "Ты кто? Оо")


@bot.message_handler(is_admin=True, commands=["addgroup"])
async def handle_add_group(message: Message):
    await bot.set_state(
        message.from_user.id,
        GroupStates.INPUT_NAME,
        message.chat.id,
    )
    await bot.send_message(
        message.chat.id,
        "Введите название группы:",
    )


@bot.message_handler(state=GroupStates.INPUT_NAME)
async def handle_group_name(message: Message):
    group_name = message.text
    if crud.check_group(group_name):
        await bot.send_message(
            message.chat.id,
            "Группа с таким названием уже существует",
        )
    else:
        crud.add_group(group_name)
        await bot.send_message(
            message.chat.id,
            "Группа успешно добавлена",
        )
        await bot.delete_state(
            message.from_user.id,
            message.chat.id,
        )
