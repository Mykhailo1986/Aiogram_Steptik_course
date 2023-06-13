from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Text
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message)

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
import sys
sys.path.append(".")
from config import TOKEN as API_TOKEN

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

# Инициализируем объект билдера
kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

# Создаем первый список с кнопками
buttons_1: list[InlineKeyboardButton] = [InlineKeyboardButton(

                 text=f'Кнопка {i + 1}',
                 callback_data=f'Button {i + 1}') for i in range(6)]


# # Создаем второй список с кнопками
buttons_2: list[InlineKeyboardButton] = [InlineKeyboardButton(
                text=f'Кнопка {i + 1}',
                 callback_data=f'Button {i + 1}') for i in range(10)]
# Распаковываем список с кнопками в билдер методом row,
# указываем, что в одном ряду должно быть 4 кнопки
kb_builder.row(*buttons_1, width=4)
# Распаковываем второй список с кнопками методом add
kb_builder.add(*buttons_2)
# Явно сообщаем билдеру сколько хотим видеть кнопок в 1-м и 2-м рядах,
# а также говорим методу повторять такое размещение для остальных рядов
kb_builder.adjust(2, 1, repeat=True)

# print(kb_builder.export())

# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру
@dp.message(CommandStart())
async def process_start_command(message: Message):
    # Методом as_markup() передаем клавиатуру как аргумент туда, где она требуется
    # await message.answer(text='Вот такая получается клавиатура',photo =	"AQADJcwxG11eMUh4",
    #                     reply_markup=kb_builder.as_markup())
    """ братите внимание, что параметр resize_keyboard=True, отвечающий за размер кнопок, который мы раньше передавали в ReplyKeyboardMarkup, теперь передается в метод билдера as_markup(), который, по сути, и превращает билдер в объект клавиатуры ReplyKeyboardMarkup."""
    # Reduce the height of the buttons
    await message.answer_photo(photo="AgACAgIAAxkBAAI_12SF8RPbsNcVCku4SK0jieBT8V75AAIlzDEbXV4xSM8Tr9fTJ-K-AQADAgADcwADLwQ",reply_markup=kb_builder.as_markup(),caption='Dflz')

if __name__ == '__main__':
    dp.run_polling(bot)