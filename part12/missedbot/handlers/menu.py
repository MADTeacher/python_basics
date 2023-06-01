from enum import Enum, auto

from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton

from missedbot import bot
from missedbot.handlers.download_report import start_download_report
from missedbot.handlers.interactive_report import start_interactive_report
from missedbot.handlers.presence_check import presence_check


class AdminException(Exception):
    ...


class Command(Enum):
    DOWNLOAD_SHORT_REPORT = auto()
    DOWNLOAD_FULL_REPORT = auto()
    INTERACTIVE_REPORT = auto()
    PRESENCE_CHECK = auto()


__admin_commands = {
    Command.DOWNLOAD_SHORT_REPORT: "Краткий отчет",
    Command.DOWNLOAD_FULL_REPORT: "Полный отчет",
    Command.INTERACTIVE_REPORT: "Интерактивный отчет",
    Command.PRESENCE_CHECK: "Проверка присутствия",
}


def menu_keyboard() -> ReplyKeyboardMarkup:
    """
    Генерирует объект ReplyKeyboardMarkup, содержащий опции меню для администратора.

    :return: Объект ReplyKeyboardMarkup, содержащий опции меню администратора.
    :rtype: ReplyKeyboardMarkup
    """

    markup = ReplyKeyboardMarkup(row_width=3)
    markup.add(
        KeyboardButton(
            __admin_commands[Command.PRESENCE_CHECK],
        ),
    )
    markup.add(
        KeyboardButton(
            __admin_commands[Command.DOWNLOAD_SHORT_REPORT],
        ),
        KeyboardButton(
            __admin_commands[Command.DOWNLOAD_FULL_REPORT],
        ),
    )
    markup.add(
        KeyboardButton(
            __admin_commands[Command.INTERACTIVE_REPORT],
        ),
    )
    return markup


def is_admin_command(command: str) -> bool:
    """
    Проверяет, является ли указанная команда командой администратора, ища ее в словаре __admin_commands.

    :param command: Строка, представляющая проверяемую команду.
    :type command: str
    :return: Булево значение, указывающее, является ли команда командой администратора.
    :rtype: bool
    """
    for key, value in __admin_commands.items():
        if value == command:
            return True
    return False


def get_current_admin_command(command: str) -> Command:
    """
    Возвращает ключ команды, если она есть в словаре __admin_commands, в противном случае
    вызывается исключение AdminException.

    Args:
        command (str): Команда для поиска в словаре __admin_commands.

    Returns:
        Ключ команды, если она есть в словаре __admin_commands.

    Raises:
        AdminException: Если команда не найдена в словаре __admin_commands.

    """
    for key, value in __admin_commands.items():
        if value == command:
            return key
    raise AdminException("Неизвестная команда")


@bot.message_handler(
    is_admin=True,
    func=lambda message: is_admin_command(message.text),
)
async def handle_commands(message: Message):
    """
    Обрабатывает команды администратора, отправленные в виде
    сообщений боту. Принимает объект сообщения, и в зависимости
    от содержащейся в нем команды, вызывает
    другие функции для выполнения конкретных действий.
    Функция вызывается только если отправитель сообщения
    является администратором и текст сообщения распознан
    как команда администратора.
    Распознаваемые команды: PRESENCE_CHECK, DOWNLOAD_FULL_REPORT,
    DOWNLOAD_SHORT_REPORT и INTERACTIVE_REPORT. Для каждой команды
    вызывается определенная функция для выполнения соответствующего
    действия.

    :param message: Объект сообщения, содержащий текст команды и
    другую информацию.
    :type message: Message
    :return: None
    """

    command = get_current_admin_command(message.text)
    match command:
        case Command.PRESENCE_CHECK:
            await presence_check(message)
        case Command.DOWNLOAD_FULL_REPORT:
            await start_download_report(message, "fullReport")
        case Command.DOWNLOAD_SHORT_REPORT:
            await start_download_report(message, "shortReport")
        case Command.INTERACTIVE_REPORT:
            await start_interactive_report(message)
