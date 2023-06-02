from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Text
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

# Создаем объекты кнопок
button_1: KeyboardButton = KeyboardButton(text='Кнопка 1')
button_2: KeyboardButton = KeyboardButton(text='Кнопка 2')
button_3: KeyboardButton = KeyboardButton(text='Кнопка 3')
button_4: KeyboardButton = KeyboardButton(text='Кнопка 4')
button_5: KeyboardButton = KeyboardButton(text='Кнопка 5')
button_6: KeyboardButton = KeyboardButton(text='Кнопка 6')
button_7: KeyboardButton = KeyboardButton(text='Кнопка 7')
button_8: KeyboardButton = KeyboardButton(text='Кнопка 8')
button_9: KeyboardButton = KeyboardButton(text='Кнопка 9')

# Создаем объект клавиатуры, добавляя в него кнопки
my_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                        keyboard=[[button_1, button_2, button_3],
                                  [button_4, button_5, button_6],
                                  [button_7, button_8, button_9]],
                        resize_keyboard=True)

# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Ось така клавіатура вийшла',
                         reply_markup=my_keyboard)


if __name__ == '__main__':
    dp.run_polling(bot)