from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
import sys
sys.path.append(".")
from config import TOKEN as API_TOKEN , USER_ID as user_id

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
# API_TOKEN: str =  ' BOT TOKEN HERE'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

# Создаем объекты инлайн-кнопок
big_button_1: InlineKeyboardButton = InlineKeyboardButton(
    text='БОЛЬШАЯ КНОПКА 1',
    callback_data='big_button_1_pressed')

big_button_2: InlineKeyboardButton = InlineKeyboardButton(
    text='БОЛЬШАЯ КНОПКА 2',
    callback_data='big_button_2_pressed')

# Создаем объект инлайн-клавиатуры
keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[big_button_1],
                     [big_button_2]])


# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру с инлайн-кнопками
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Это инлайн-кнопки. Нажми на любую!',
                         reply_markup=keyboard)


if __name__ == '__main__':
    dp.run_polling(bot)