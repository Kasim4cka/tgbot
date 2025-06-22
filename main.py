import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

# Замените этот токен на ваш реальный токен бота из BotFather
TOKEN = '8066286253:AAEcsbSTjqUXmMq14tGyknh85m6oiwf6_lo'

# Замените 'ВАША_ССЫЛКА_НА_ГРУППУ' на реальную ссылку на вашу Telegram-группу.
# Это может быть "t.me/имя_вашей_группы" или ссылка-приглашение.
TELEGRAM_GROUP_LINK = 'https://t.me/+KmXKuPzRICk0ODEy' # <<< ОБЯЗАТЕЛЬНО ИЗМЕНИТЕ ЭТО

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    # Создаем кнопку
    button = InlineKeyboardButton(text="Перейти в группу", url=TELEGRAM_GROUP_LINK)
    # Создаем клавиатуру с одной кнопкой
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button]])

    # Отправляем сообщение с текстом и клавиатурой
    await message.answer(
        f"Привет, {html.bold(message.from_user.full_name)}!\n\n"
        "Нажмите кнопку ниже, чтобы перейти в нашу Telegram-группу:",
        reply_markup=keyboard
    )

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
