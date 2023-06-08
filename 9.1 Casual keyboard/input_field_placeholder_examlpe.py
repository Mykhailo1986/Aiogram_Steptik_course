from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType, KeyboardButtonRequestUser
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

# Инициализируем билдер
kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Создаем кнопки
btn_1: KeyboardButton = KeyboardButton(text='Кнопка 1')
btn_2: KeyboardButton = KeyboardButton(text='Кнопка 2')

# Создаем объект клавиатуры
placeholder_exmpl_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[btn_1, btn_2]],
                                    resize_keyboard=True,
                                    input_field_placeholder='Нажмите кнопку 1')


# Этот хэндлер будет срабатывать на команду "/placeholder"
@dp.message(Command(commands='placeholder'))
async def process_placeholder_command(message: Message):
    await message.answer(text='Экспериментируем с полем placeholder',
                         reply_markup=placeholder_exmpl_kb)

if __name__ == '__main__':
    dp.run_polling(bot)