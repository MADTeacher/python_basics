from telebot.types import Message, BotCommand, BotCommandScope

from missedbot import bot
from missedbot.handlers.menu import menu_keyboard


@bot.message_handler(is_admin=True, commands=["start"])
async def handle_start(message: Message):
    """
    Обрабатывает команду 'start' для администраторов. 
    Устанавливает команды бота и отправляет приветственное 
    сообщение с меню-клавиатурой.
    """
    await bot.set_my_commands(
        commands=[
            BotCommand('addstudent', 'Добавить студента'),
            BotCommand('adddiscipline', 'Добавить дисциплину'),
            BotCommand('discipline2group', 'Назначить дисциплину группе'),
            BotCommand('addgroup', 'Добавить группу'),
            BotCommand('fullreport', 'Полный отчет'),
            BotCommand('shortreport', 'Краткий отчет'),
            BotCommand('interreport', 'Интерактивный отчет'),
            BotCommand('presencecheck', 'Проверка присутствия'),
            BotCommand('delstudent', 'Удалить студента'),
        ],
        language_code='ru',
        scope=BotCommandScope(
            user_id=message.from_user.id,
            chat_id=message.chat.id,
        )
    )
    await bot.send_message(
                message.chat.id,
                "<b>Поехали!!!</b>",
                parse_mode="HTML",
                disable_web_page_preview=True,
                reply_markup=menu_keyboard(),
            )


@bot.message_handler(is_admin=False, commands=['start'])
async def handle_no_add_teacher(message: Message):
    """
    Декоратор для обработки команды '/start' для пользователей, 
    не являющихся администраторами. 
    Он отправляет сообщение 'Ты кто? Оо' в чат пользователя.
    """
    await bot.send_message(message.chat.id, "Ты кто? Оо")