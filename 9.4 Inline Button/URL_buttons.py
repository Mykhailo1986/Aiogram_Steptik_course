from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
import sys
sys.path.append(".")
from config import TOKEN as API_TOKEN , USER_ID as user_id

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
# API_TOKEN: str =  '8'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

async def start() -> InlineKeyboardMarkup:
    # Создаем объекты инлайн-кнопок
    url_button_1: InlineKeyboardButton = InlineKeyboardButton(
        text='Курс "Телеграм-боты на Python и AIOgram"',
        url='https://stepik.org/120924')
    url_button_2: InlineKeyboardButton = InlineKeyboardButton(
        text='Документация Telegram Bot API',
        url='https://core.telegram.org/bots/api')

    # Создаем объект инлайн-клавиатуры
    keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
        inline_keyboard=[[url_button_1],
                        [url_button_2]])
    return keyboard



async def tg()-> InlineKeyboardMarkup:
    # Создаем объекты инлайн-кнопок
    group_name = 'aiogram_stepik_course'
    url_button_1: InlineKeyboardButton = InlineKeyboardButton(
                                        text='Группа "Телеграм-боты на AIOgram"',
                                        url=f'tg://resolve?domain={group_name}')
    # user_id = 617409965
    url_button_2: InlineKeyboardButton = InlineKeyboardButton(
                                        text='Автор курса на Степике по телеграм-ботам',
                                        url=f'tg://user?id={user_id}')

    channel_name = 'toBeAnMLspecialist'
    url_button_3: InlineKeyboardButton = InlineKeyboardButton(
                                        text='Канал "Стать специалистом по машинному обучению"',
                                        url=f'https://t.me/{channel_name}')

    # Создаем объект инлайн-клавиатуры
    keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
        inline_keyboard=[[url_button_1],
                        [url_button_2],
                        [url_button_3]])
    return keyboard


@dp.message(CommandStart())
async def process_start_command(message: Message):
    keyboard = await start2()
    await message.answer(text='Это инлайн-кнопки с параметром "url"',
                         reply_markup=keyboard)


@dp.message(Command(commands=['tg']))
async def process_tg(message: Message):
    keyboard = await tg()
    await message.answer(text='Это инлайн-кнопки с параметром "url" по протоколу tg:// - это специальный протокол самого телеграм, позволяющий открывать ссылки, даже если домен t.me заблокирован ',
                         reply_markup=keyboard)

if __name__ == '__main__':
    dp.run_polling(bot)