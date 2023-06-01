import asyncio
import pathlib

from telebot.types import (
    InputFile,
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

import database.crud as crud
from missedbot import bot
from report.run_report_builder import (
    run_report_builder,
    ReportBuilderTypeEnum,
)

__report_prefix = [
    "fullReport_",
    "fullGrReport_",
    "shortReport_",
    "shortGrReport_",
]

__next_step = {
    "fullReport": "fullGrReport",
    "shortReport": "shortGrReport",
}


__reports_builder_type = {
    "fullGrReport": ReportBuilderTypeEnum.FULL,
    "shortGrReport": ReportBuilderTypeEnum.SHORT,
}


def __is_download_prefix_callback(data: str) -> bool:
    for it in __report_prefix:
        if it in data:
            return True
    return False


@bot.message_handler(
    is_admin=False,
    commands=["fullreport"],
)
async def handle_no_full_report(message: Message):
    await bot.send_message(message.chat.id, "Ты кто? Оо")


@bot.message_handler(
    is_admin=True,
    commands=["fullreport"],
)
async def handle_full_report(message: Message):
    await start_download_report(message, "fullReport")


@bot.message_handler(
    is_admin=False,
    commands=["shortreport"],
)
async def handle_no_short_report(message: Message):
    await bot.send_message(message.chat.id, "Ты кто? Оо")


@bot.message_handler(
    is_admin=True,
    commands=["shortreport"],
)
async def handle_short_report(message: Message):
    await start_download_report(message, "shortReport")


async def start_download_report(
    message: Message,
    prefix: str = None,
):
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
    await bot.send_message(
        message.chat.id,
        "Выберете группу:",
        reply_markup=markup,
    )


@bot.callback_query_handler(
    func=lambda call: __is_download_prefix_callback(call.data),
)
async def callback_download_full_report(call: CallbackQuery):
    type_callback = call.data.split("_")[0]
    match type_callback:
        case "fullReport" | "shortReport":
            await bot.edit_message_text(
                "Выберете предмет",
                call.message.chat.id,
                call.message.id,
            )
            group_id = int(call.data.split("_")[1])
            disciplines = crud.get_assigned_discipline(group_id)

            if len(disciplines) == 0:
                await bot.edit_message_text(
                    "За группой не числится дисциплин",
                    call.message.chat.id,
                    call.message.id,
                )
            elif len(disciplines) > 1:
                markup = InlineKeyboardMarkup()
                markup.row_width = 1
                markup.add(
                    *[
                        InlineKeyboardButton(
                            it.name,
                            callback_data=f"fullGrReport_{group_id}_{it.id}",
                        )
                        for it in disciplines
                    ]
                )
                await bot.edit_message_text(
                    "Выберите дисциплину:",
                    call.message.chat.id,
                    call.message.id,
                    reply_markup=markup,
                )
            else:
                await __create_report(
                    call,
                    group_id,
                    disciplines[0].id,
                    __reports_builder_type[__next_step[type_callback]],
                )

        case "fullGrReport" | "shortGrReport":
            group_id = int(call.data.split("_")[1])
            discipline_id = int(call.data.split("_")[2])
            await __create_report(
                call,
                group_id,
                discipline_id,
                __reports_builder_type[type_callback],
            )

        case _:
            await bot.edit_message_text(
                "Неизвестный формат для обработки данных",
                call.message.chat.id,
                call.message.id,
            )


async def __create_report(
    call: CallbackQuery,
    group_id: int,
    discipline_id: int,
    builder_type: ReportBuilderTypeEnum,
) -> None:
    await bot.edit_message_text(
        "Начинаем формировать отчет",
        call.message.chat.id,
        call.message.id,
    )

    path_to_report = await asyncio.gather(
        asyncio.to_thread(
            run_report_builder,
            group_id,
            discipline_id,
            builder_type,
        )
    )

    await bot.edit_message_text(
        "Отчет успешно сформирован",
        call.message.chat.id,
        call.message.id,
    )

    await bot.send_document(
        call.message.chat.id,
        InputFile(
            pathlib.Path(path_to_report[0]),
        ),
    )
