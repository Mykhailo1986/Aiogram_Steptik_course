
from config import TOKEN
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ContentType
from aiogram import F

# Замість BOT TOKEN HERE потрібно вставити токен вашого бота, отриманого від @BotFather
API_TOKEN: str = TOKEN

# Створюємо об'єкти бота і диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


# Цей хендлер буде викликаний на команду "/start"

async def process_start_command(message: Message):
    await message.answer('Привіт!\nМене звуть Ехо-бот!\nНапиши мені щось')


# Цей хендлер буде викликаний на команду "/help"

async def process_help_command(message: Message):
    await message.answer('Напиши мені щось і відповім тобі твоє повідомлення')

# Цей хендлер буде викликаний на відправку фото
async def send_photo_echo(message: Message):
    print(message)
    await message.reply_photo(message.photo[0].file_id)


# Цей хендлер буде викликаний на будь-які ваші текстові повідомлення,
# окрім команд "/start" і "/help"

async def send_echo(message: Message):
    text: str = f"Усі кажуть {message.text.lower()}"

    await message.reply(text=text)
    # await bot.send_message(chat_id='ID чи назва чату', text='текст')
    # await bot.send_message(message.chat.id, message.text)



# Реєструємо хендлери
dp.message.register(process_start_command, Command(commands=["start"]))
dp.message.register(process_help_command, Command(commands=['help']))
# dp.message.register(send_photo_echo, F.content_type == ContentType.PHOTO)
dp.message.register(send_photo_echo, F.photo) # коротший вид запису
dp.message.register(send_echo)

if __name__ == '__main__':
    dp.run_polling(bot)
