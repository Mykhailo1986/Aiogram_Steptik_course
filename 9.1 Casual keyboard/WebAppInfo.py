from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Text, Command
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

import sys
sys.path.append(".")
from config import TOKEN

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
API_TOKEN: str = TOKEN

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()





from aiogram.types.web_app_info import WebAppInfo


# Создаем кнопку
web_app_btn: KeyboardButton = KeyboardButton(
                                text='Start Web App',
                                web_app=WebAppInfo(url="https://stepik.org/"))

# Создаем объект клавиатуры
web_app_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                            keyboard=[[web_app_btn]],
                                            resize_keyboard=True)


# Этот хэндлер будет срабатывать на команду "/web_app"
@dp.message(Command(commands='web_app'))
async def process_web_app_command(message: Message):
    await message.answer(text='Экспериментируем со специальными кнопками',
                         reply_markup=web_app_keyboard)

if __name__ == '__main__':
    dp.run_polling(bot)