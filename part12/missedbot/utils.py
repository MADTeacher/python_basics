from telebot.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from database import crud


def create_group_inline_button(
    prefix: str,
) -> InlineKeyboardMarkup:
    groups = crud.get_groups()
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        *[
            InlineKeyboardButton(
                it.name,
                callback_data=f"{prefix}_{it.id}",
            )
            for it in groups
        ]
    )
    return markup


def create_discipline_inline_button(
    prefix: str,
) -> InlineKeyboardMarkup:
    disciplines = crud.get_disciplines()
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        *[
            InlineKeyboardButton(
                it.name,
                callback_data=f"{prefix}_{it.id}",
            )
            for it in disciplines
        ]
    )
    return markup
