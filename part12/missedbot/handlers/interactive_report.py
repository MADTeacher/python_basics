from telebot.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from database import crud
from missedbot import bot

PAGINATOR = 7


@bot.message_handler(
        is_admin=False, 
        commands=["interreport"],
)
async def handle_no_interactive_report(message: Message):
    await bot.send_message(message.chat.id, "Ты кто? Оо")


@bot.message_handler(
        is_admin=True, 
        commands=["interreport"],
)
async def handle_interactive_report(message: Message):
    await start_interactive_report(message)


async def start_interactive_report(message: Message):
    disciplines = crud.get_disciplines()
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        *[
            InlineKeyboardButton(
                it.name,
                callback_data=f"disReport_{it.id}",
            )
            for it in disciplines
        ]
    )
    await bot.send_message(
        message.chat.id,
        "Выберете дисциплину:",
        reply_markup=markup,
    )


@bot.callback_query_handler(
    func=lambda call: ("disReport_" in call.data 
                       or "groupReport_" in call.data),)
async def callback_interactive_report(call):
    step = call.data.split("_")[0]
    match step:
        case "disReport":
            discipline_id = int(call.data.split("_")[1])
            groups = crud.get_assigned_group(discipline_id)
            markup = InlineKeyboardMarkup()
            markup.row_width = 1
            markup.add(
                *[
                    InlineKeyboardButton(
                        it.name, 
                        callback_data=f"groupReport_0_{it.id}_{discipline_id}",
                    )
                    for it in groups
                ]
            )
            await bot.edit_message_text(
                "Выберете студента",
                call.message.chat.id,
                call.message.id,
                reply_markup=markup,
            )
        case "groupReport":
            paginator = int(call.data.split("_")[1])
            group_id = int(call.data.split("_")[2])
            discipline_id = int(call.data.split("_")[3])
            students = crud.get_students(group_id)

            markup = InlineKeyboardMarkup()
            markup.row_width = 1
            markup.add(
                *[
                    InlineKeyboardButton(
                        f"{it.full_name}",
                        callback_data=f"studRepClick_{it.id}_{discipline_id}",
                    )
                    for it in students[
                        PAGINATOR * paginator : PAGINATOR * (paginator + 1)
                    ]
                ]
            )
            if paginator == 0:
                markup.add(
                    InlineKeyboardButton(
                        "➡",
                        callback_data=f"groupReport_{paginator + 1}_{group_id}_{discipline_id}",
                    )
                )
            elif len(students) > PAGINATOR * (paginator + 1):
                markup.add(
                    InlineKeyboardButton(
                        "⬅",
                        callback_data=f"groupReport_{paginator - 1}_{group_id}_{discipline_id}",
                    ),
                    InlineKeyboardButton(
                        "➡",
                        callback_data=f"groupReport_{paginator + 1}_{group_id}_{discipline_id}",
                    ),
                    row_width=2,
                )
            else:
                markup.add(
                    InlineKeyboardButton(
                        "⬅",
                        callback_data=f"groupReport_{paginator - 1}_{group_id}_{discipline_id}",
                    )
                )
            await bot.edit_message_text(
                "Выберете студента",
                call.message.chat.id,
                call.message.id,
                reply_markup=markup,
            )


@bot.callback_query_handler(
    func=lambda call: "studRepClick_" in call.data,
)
async def callback_student_report(call):
    student_id = int(call.data.split("_")[1])
    discipline_id = int(call.data.split("_")[2])
    result = crud.get_academic_performance(
        student_id, 
        discipline_id,
        )
    text = f"Студент: {result[0]}\n"
    text += f"Пропущено занятий: {result[1]}\n"
    text += f"Всего занятий: {result[2]}\n"
    await bot.edit_message_text(
        text,
        call.message.chat.id,
        call.message.id,
    )
