from telebot.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from database import crud
from missedbot import bot
from missedbot.utils import create_discipline_inline_button


@bot.message_handler(
    is_admin=False,
    commands=["discipline2group"],
)
async def handle_no_discipline2group(message: Message):
    await bot.send_message(message.chat.id, "Ты кто? Оо")


@bot.message_handler(
    is_admin=True,
    commands=["discipline2group"],
)
async def handle_discipline2group(message: Message):
    markup = create_discipline_inline_button("dis2group")
    await bot.send_message(
        message.chat.id,
        "Выбурете дисциплину:",
        reply_markup=markup,
    )


@bot.callback_query_handler(
    func=lambda call: "dis2group_" in call.data,
)
async def callback_search_groups(call):
    discipline_id = int(call.data.split("_")[1])
    groups = crud.get_groups_without_discipline(discipline_id)
    if not groups:
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Нет групп для назначения",
        )
        return
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        *[
            InlineKeyboardButton(
                it.name,
                callback_data=f"applygroup_{discipline_id}_{it.id}",
            )
            for it in groups
        ]
    )
    await bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text="Выберете группу:",
        reply_markup=markup,
    )


@bot.callback_query_handler(
    func=lambda call: "applygroup_" in call.data,
)
async def callback_discipline2group(call):
    discipline_id = int(call.data.split("_")[1])
    group_id = int(call.data.split("_")[2])
    crud.set_discipline2group(discipline_id, group_id)
    await bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text="Дисциплина назначена группе",
    )
