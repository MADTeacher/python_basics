import re

from telebot.asyncio_handler_backends import StatesGroup, State
from telebot.types import Message

from database import crud
from missedbot import bot
from missedbot.utils import create_group_inline_button


class StudentStates(StatesGroup):
    INPUT_NAME = State()


@bot.message_handler(is_admin=False, commands=["addstudent"])
async def handle_no_add_student(message: Message):
    await bot.send_message(message.chat.id, "Ты кто? Оо")


@bot.message_handler(is_admin=True, commands=["addstudent"])
async def handle_add_student(message: Message):
    markup = create_group_inline_button("groupClick")
    await bot.send_message(
        message.chat.id,
        "Выберете группу:",
        reply_markup=markup,
    )


@bot.callback_query_handler(func=lambda call: "groupClick_" in call.data)
async def callback_group_choose(call):
    await bot.set_state(
        call.from_user.id,
        StudentStates.INPUT_NAME,
        call.message.chat.id,
    )
    async with bot.retrieve_data(
        call.from_user.id,
        call.message.chat.id,
    ) as data:
        data["group_id"] = int(call.data.split("_")[1])
    
    await bot.edit_message_text(
        "Введите ФИО студента",
        call.message.chat.id,
        call.message.id,
    )


@bot.message_handler(state=StudentStates.INPUT_NAME)
async def handle_student_name(message: Message):
    full_name = message.text
    if not re.match(
        r"^[А-ЯЁ][а-яё]+\s[А-ЯЁ][а-яё]+\s[А-ЯЁ][а-яё]+$",
        full_name,
    ):
        await bot.send_message(
            message.chat.id,
            "Пожалуйста, введите ФИО формате: Иванов Иван Иванович",
        )
        return
    
    async with bot.retrieve_data(
        message.from_user.id,
        message.chat.id,
    ) as data:
        group_id = data["group_id"]

    crud.add_student(group_id, full_name)
    await bot.delete_state(
        message.from_user.id,
        message.chat.id,
    )
