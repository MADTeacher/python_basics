from telebot.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from database import crud
from missedbot import bot
from missedbot.utils import create_group_inline_button


PAGINATOR = 7


@bot.message_handler(is_admin=False, commands=["delstudent"])
async def handle_no_del_student(message: Message):
    await bot.send_message(message.chat.id, "Ты кто? Оо")


@bot.message_handler(is_admin=True, commands=["delstudent"])
async def handle_del_student(message: Message):
    markup = create_group_inline_button("groupForDelClick_0")
    await bot.send_message(
        message.chat.id,
        "Выберете группу:",
        reply_markup=markup,
    )


@bot.callback_query_handler(
    func=lambda call: "groupForDelClick_" in call.data,
)
async def callback_choose_student(call):
    paginator = int(call.data.split("_")[1])
    group_id = int(call.data.split("_")[2])
    students = crud.get_students(group_id)

    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        *[
            InlineKeyboardButton(
                f"{it.full_name}",
                callback_data=f"studDelClick_{it.id}",
            )
            for it in students[PAGINATOR * paginator : PAGINATOR * (paginator + 1)]
        ]
    )
    if paginator == 0:
        markup.add(
            InlineKeyboardButton(
                "➡",
                callback_data=f"groupForDelClick_{paginator + 1}_{group_id}",
            )
        )
    elif len(students) > PAGINATOR * (paginator + 1):
        markup.add(
            InlineKeyboardButton(
                "⬅",
                callback_data=f"groupForDelClick_{paginator - 1}_{group_id}",
            ),
            InlineKeyboardButton(
                "➡",
                callback_data=f"groupForDelClick_{paginator + 1}_{group_id}",
            ),
            row_width=2,
        )
    else:
        markup.add(
            InlineKeyboardButton(
                "⬅",
                callback_data=f"groupForDelClick_{paginator - 1}_{group_id}",
            )
        )
    await bot.edit_message_text(
        "Выберете удаляемого студента",
        call.message.chat.id,
        call.message.id,
        reply_markup=markup,
    )


@bot.callback_query_handler(
    func=lambda call: "studDelClick_" in call.data,
)
async def callback_del_student(call):
    student_id = int(call.data.split("_")[1])
    crud.remove_student(student_id)
    await bot.edit_message_text(
        "Студент удален",
        call.message.chat.id,
        call.message.id,
    )
