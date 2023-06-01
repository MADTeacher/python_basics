from telebot.asyncio_handler_backends import StatesGroup, State
from telebot.types import Message

from database import crud
from missedbot import bot


class DisciplineStates(StatesGroup):
    INPUT_NAME = State()


@bot.message_handler(
    is_admin=False,
    commands=["adddiscipline"],
)
async def handle_no_add_discipline(message: Message):
    await bot.send_message(message.chat.id, "Ты кто? Оо")


@bot.message_handler(
    is_admin=True,
    commands=["adddiscipline"],
)
async def handle_add_discipline(message: Message):
    await bot.set_state(
        message.from_user.id,
        DisciplineStates.INPUT_NAME,
        message.chat.id,
    )
    await bot.send_message(
        message.chat.id,
        "Введите название дисциплины:",
    )


@bot.message_handler(state=DisciplineStates.INPUT_NAME)
async def handle_discipline_name(message: Message):
    discipline_name = message.text
    if crud.check_discipline(discipline_name):
        await bot.send_message(
            message.chat.id,
            "Дисциплина с таким названием уже существует",
        )
    else:
        crud.add_discipline(discipline_name)
        await bot.send_message(
            message.chat.id,
            "Дисциплина успешно добавлена",
        )
        await bot.delete_state(
            message.from_user.id,
            message.chat.id,
        )
