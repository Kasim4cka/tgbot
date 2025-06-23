import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

# Замените этот токен на ваш реальный токен бота из BotFather
TOKEN = '8066286253:AAEcsbSTjqUXmMq14tGyknh85m6oiwf6_lo'

# --- ССЫЛКИ ДЛЯ ВАРИАНТА "Перейти в группу" (по умолчанию) ---
# Эта ссылка используется для самой первой кнопки "Перейти в группу (Основная)"
DEFAULT_TELEGRAM_GROUP_LINK = 'https://t.me/driftnolegal' # <<< ОБЯЗАТЕЛЬНО ИЗМЕНИТЕ ЭТО

# --- ССЫЛКИ ДЛЯ ВАРИАНТА "Получить ссылку (Вариант 1)" ---
# Эти ссылки будут отправлены, когда пользователь нажмет "Получить ссылку (Вариант 1)"
TELEGRAM_GROUP_LINK_OPTION1 = 'https://t.me/your_group_link_option1' # <<< ССЫЛКА НА ГРУППУ ДЛЯ ВАРИАНТА 1
DOCUMENT_LINK_OPTION1 = 'https://disk.yandex.ru/d/7vgFivzNrCvORQ' # <<< ССЫЛКА НА ДОКУМЕНТ ДЛЯ ВАРИАНТА 1

# --- ССЫЛКИ ДЛЯ ВАРИАНТА "Получить ссылку (Вариант 2)" ---
# Эти ссылки будут отправлены, когда пользователь нажмет "Получить ссылку (Вариант 2)"
TELEGRAM_GROUP_LINK_OPTION2 = 'https://t.me/+c1AbIAQvWQllNTBi' # <<< ССЫЛКА НА ГРУППУ ДЛЯ ВАРИАНТА 2
DOCUMENT_LINK_OPTION2 = 'https://disk.yandex.ru/i/rhGtp75L4sFfQQ' # <<< ССЫЛКА НА ДОКУМЕНТ ДЛЯ ВАРИАНТА 2


# --- Конфигурация кнопок ---
# Здесь вы можете настроить текст для всех кнопок в боте.
BUTTON_TEXT_DIRECT_LINK = "Основное сообщество"
BUTTON_TEXT_SEND_LINK_1 = "RDS GP"
BUTTON_TEXT_SEND_LINK_2 = "RDS OPEN"
BUTTON_TEXT_GO_TO_GROUP = "Смотреть в TG" # Текст для кнопки внутри сообщения со ссылкой на группу
BUTTON_TEXT_GO_TO_DOCUMENT = "Cмотреть Ydisk" # Текст для кнопки со ссылкой на документ
# --- Конец конфигурации кнопок ---

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    # Создаем кнопки для стартового меню
    # Первая кнопка ведет на основную группу
    button_direct_link = InlineKeyboardButton(text=BUTTON_TEXT_DIRECT_LINK, url=DEFAULT_TELEGRAM_GROUP_LINK)
    # Кнопка для получения ссылок Варианта 1
    button_send_link_1 = InlineKeyboardButton(text=BUTTON_TEXT_SEND_LINK_1, callback_data="option_1_links")
    # Кнопка для получения ссылок Варианта 2
    button_send_link_2 = InlineKeyboardButton(text=BUTTON_TEXT_SEND_LINK_2, callback_data="option_2_links")

    # Создаем клавиатуру с тремя кнопками, каждая на новой строке
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [button_direct_link],
        [button_send_link_1],
        [button_send_link_2]
    ])

    # Отправляем приветственное сообщение с текстом и клавиатурой
    await message.answer(
        f"Привет, {html.bold(message.from_user.full_name)}!\n\n"
        "Выберите действие ниже:",
        reply_markup=keyboard
    )

# --- Хэндлер для "Получить ссылку (Вариант 1)" ---
@dp.callback_query(lambda c: c.data == 'option_1_links')
async def process_option_1_links(callback_query: CallbackQuery):
    # Создаем кнопку "Перейти в группу" для сообщения со ссылкой на группу (Вариант 1)
    group_button = InlineKeyboardButton(text=BUTTON_TEXT_GO_TO_GROUP, url=TELEGRAM_GROUP_LINK_OPTION1)
    group_keyboard = InlineKeyboardMarkup(inline_keyboard=[[group_button]])

    # Отправляем сообщение со ссылкой на группу и кнопкой (Вариант 1)
    await callback_query.message.answer(
        f"RDS GP: {TELEGRAM_GROUP_LINK_OPTION1}\n\n"
        "Нажмите кнопку, чтобы перейти:",
        reply_markup=group_keyboard
    )

    # Создаем кнопку "Открыть документ" для сообщения со ссылкой на документ (Вариант 1)
    document_button = InlineKeyboardButton(text=BUTTON_TEXT_GO_TO_DOCUMENT, url=DOCUMENT_LINK_OPTION1)
    document_keyboard = InlineKeyboardMarkup(inline_keyboard=[[document_button]])

    # Отправляем ОТДЕЛЬНЫМ сообщением ссылку на документ с кнопкой (Вариант 1)
    await callback_query.message.answer(
        f"Ydisk: {DOCUMENT_LINK_OPTION1}\n\n"
        "Нажмите кнопку, чтобы открыть его:",
        reply_markup=document_keyboard
    )

    # Обязательно отвечаем на callback-запрос, чтобы убрать состояние "загрузки" с кнопки
    await callback_query.answer()

# --- Хэндлер для "Получить ссылку (Вариант 2)" ---
@dp.callback_query(lambda c: c.data == 'option_2_links')
async def process_option_2_links(callback_query: CallbackQuery):
    # Создаем кнопку "Перейти в группу" для сообщения со ссылкой на группу (Вариант 2)
    group_button = InlineKeyboardButton(text=BUTTON_TEXT_GO_TO_GROUP, url=TELEGRAM_GROUP_LINK_OPTION2)
    group_keyboard = InlineKeyboardMarkup(inline_keyboard=[[group_button]])

    # Отправляем сообщение со ссылкой на группу и кнопкой (Вариант 2)
    await callback_query.message.answer(
        f"RDS OPEN: {TELEGRAM_GROUP_LINK_OPTION2}\n\n"
        "Нажмите кнопку, чтобы перейти:",
        reply_markup=group_keyboard
    )

    # Создаем кнопку "Открыть документ" для сообщения со ссылкой на документ (Вариант 2)
    document_button = InlineKeyboardButton(text=BUTTON_TEXT_GO_TO_DOCUMENT, url=DOCUMENT_LINK_OPTION2)
    document_keyboard = InlineKeyboardMarkup(inline_keyboard=[[document_button]])

    # Отправляем ОТДЕЛЬНЫМ сообщением ссылку на документ с кнопкой (Вариант 2)
    await callback_query.message.answer(
        f"Ydisk: {DOCUMENT_LINK_OPTION2}\n\n"
        "Нажмите кнопку, чтобы открыть его:",
        reply_markup=document_keyboard
    )

    # Обязательно отвечаем на callback-запрос
    await callback_query.answer()

@dp.message()
async def echo_handler(message: Message) -> None:
    # Этот хэндлер будет отвечать "Nice try!" на все остальные сообщения,
    # если они не являются командой /start и не могут быть скопированы.
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
