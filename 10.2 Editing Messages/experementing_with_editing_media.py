from aiogram import Bot, Dispatcher
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, InputMediaAudio,
                           InputMediaDocument, InputMediaPhoto,
                           InputMediaVideo, Message)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import CommandStart, Text
from aiogram.exceptions import TelegramBadRequest
import sys
sys.path.append(".")
from config import TOKEN as BOT_TOKEN
# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
# BOT_TOKEN = 'BOT TOKEN HERE'
# BOT_TOKEN = '5424991242:AAFbT6ckF2HYKPDyLWLFvx5C2jV71TsG9vQ'

bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher()


LEXICON: dict[str, str] = {
    'audio': '🎶 Аудио',
    'text': '📃 Текст',
    'photo': '🖼 Фото',
    'video': '🎬 Видео',
    'document': '📑 Документ',
    'voice': '📢 Голосовое сообщение',
    'text_1': 'Это обыкновенное текстовое сообщение, его можно легко отредактировать другим текстовым сообщением, но нельзя отредактировать сообщением с медиа.',
    'text_2': 'Это тоже обыкновенное текстовое сообщение, которое можно заменить на другое текстовое сообщение через редактирование.',
    'photo_id1': 'AgACAgIAAxkDAAJAzGSNfVL75vySR8mbdKkewIydHB9DAALNyDEbKlZwSB0pDisdWWzwAQADAgADdwADLwQ',
    'photo_id2': 'AgACAgIAAxkDAAJAzmSNfVLJDA5pU748kaTWEdYjZ1XpAALPyDEbKlZwSLaXSk1zK6BvAQADAgADbQADLwQ',
    'voice_id1': 'AwACAgIAAxkBAAJBvmSNvaOW5WJGaoiAyP7by6CZcGoeAAKIMgACKlZwSOId0FqOVXvELwQ',
    'voice_id2': 'AwACAgIAAxkDAAJBomSNofuXwNYSxqLYARkAAesIaiULJwACjjEAAipWcEgG3QYZ16FjtC8E',
    'audio_id1': 'CQACAgIAAxkDAAJBoWSNofvZxpFNJznw5S9TLRl3Oe-1AAKNMQACKlZwSLl3PRS-6hEBLwQ',
    'audio_id2': 'AwACAgIAAxkBAAJBvmSNvaOW5WJGaoiAyP7by6CZcGoeAAKIMgACKlZwSOId0FqOVXvELwQ',
    'document_id1': 'BQACAgIAAxkBAAJBs2SNsUTbD5EDwUdYsBNCZ69mjYhVAAIVMgACKlZwSME3yMwR3Of_LwQ',
    'document_id2': 'BQACAgIAAxkDAAJBoGSNofouvoAegpUWKePes6Ep2MSCAAKMMQACKlZwSP1R6iQ-LzkaLwQ',
    'video_id1': 'BAACAgIAAxkDAAJBqGSNof-w44M9uGnpwwABc0okbDsI9AACkDEAAipWcEgEKI3_KU4O0C8E',
    'video_id2': 'BAACAgIAAxkDAAJBp2SNof3bMqElBZEoHdeY1Y40G0b4AAKPMQACKlZwSP_XpBRfIOZOLwQ',
    }


# Функция для генерации клавиатур с инлайн-кнопками
def get_markup(width: int, *args, **kwargs) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []
    # Заполняем список кнопками из аргументов args и kwargs
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=LEXICON[button] if button in LEXICON else button,
                callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button))
    # Распаковываем список с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons, width=width)
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()



# V 9 Этот хэндлер будет срабатывать на команду "/start"
@dp.message(CommandStart())
async def process_start_command(message: Message):
    markup = get_markup(2, 'voice')
    await message.answer_audio(
                        audio=LEXICON['voice_id1'],
                        caption='Это голосовое сообщение 1',
                        reply_markup=markup)


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
@dp.callback_query(Text(text=['text',
                              'audio',
                              'video',
                              'document',
                              'photo',
                              'voice']))
async def process_button_press(callback: CallbackQuery, bot: Bot):
    markup = get_markup(2, 'voice')
    try:
        await bot.edit_message_media(
                        chat_id=callback.message.chat.id,
                        message_id=callback.message.message_id,
                        media=InputMediaAudio(
                                media=LEXICON['voice_id2'],
                                caption='Это голосове сообщение 2'),
                        reply_markup=markup)
    except TelegramBadRequest:
        await bot.edit_message_media(
                        chat_id=callback.message.chat.id,
                        message_id=callback.message.message_id,
                        media=InputMediaAudio(
                                media=LEXICON['voice_id1'],
                                caption='Это голосове сообщение 1'),
                        reply_markup=markup)
# v 3. Меняем фото на фото

# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(CommandStart())
async def process_start_command(message: Message):
    markup = get_markup(2, 'photo')
    await message.answer_photo(
                        photo=LEXICON['photo_id1'],
                        caption='Это фото 1',
                        reply_markup=markup)


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
@dp.callback_query(Text(text=['text',
                              'audio',
                              'video',
                              'document',
                              'photo',
                              'voice']))
async def process_button_press(callback: CallbackQuery, bot: Bot):
    markup = get_markup(2, 'photo')
    try:
        await bot.edit_message_media(
                            chat_id=callback.message.chat.id,
                            message_id=callback.message.message_id,
                            media=InputMediaPhoto(
                                    media=LEXICON['photo_id2'],
                                    caption='Это фото 2'),
                            reply_markup=markup)
    except TelegramBadRequest:
        await bot.edit_message_media(
                            chat_id=callback.message.chat.id,
                            message_id=callback.message.message_id,
                            media=InputMediaPhoto(
                                    media=LEXICON['photo_id1'],
                                    caption='Это фото 1'),
                            reply_markup=markup)

# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(CommandStart())
async def process_start_command(message: Message):
    markup = get_markup(2, 'text')
    await message.answer(
                    text=LEXICON['text_1'],
                    reply_markup=markup)
# v 2. Меняем текст на медиа
# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
@dp.callback_query(Text(text=['text',
                              'audio',
                              'video',
                              'document',
                              'photo',
                              'voice']))
async def process_button_press(callback: CallbackQuery, bot: Bot):
    markup = get_markup(2, 'photo')
    await bot.edit_message_media(
                        chat_id=callback.message.chat.id,
                        message_id=callback.message.message_id,
                        media=InputMediaPhoto(
                                media=LEXICON['photo_id1'],
                                caption='Это фото 1'),
                        reply_markup=markup)


# v 1. Меняем текст на текст
# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
@dp.callback_query(Text(text=['text',
                              'audio',
                              'video',
                              'document',
                              'photo',
                              'voice']))
async def process_button_press(callback: CallbackQuery):
    markup = get_markup(2, 'text')
    if callback.message.text == LEXICON['text_1']:
        text = LEXICON['text_2']
    else:
        text = LEXICON['text_1']
    await callback.message.edit_text(
                            text=text,
                            reply_markup=markup)


# Этот хэндлер будет срабатывать на все остальные сообщения
@dp.message()
async def send_echo(message: Message):
    print(message)
    await message.answer(
            text='Не понимаю')


if __name__ == '__main__':
    dp.run_polling(bot)