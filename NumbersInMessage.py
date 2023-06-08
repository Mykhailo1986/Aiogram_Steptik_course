from aiogram import Bot, Dispatcher
from aiogram.filters import BaseFilter
from aiogram.filters import Text, Command
from aiogram.types import Message
from config import TOKEN
from typing import Any

# Замість BOT TOKEN HERE потрібно вставити токен вашого бота, отриманого від @BotFather
API_TOKEN: str = TOKEN

# Створюємо об'єкти бота і диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


# Цей фільтр перевірятиме наявність невід'ємних чисел у повідомленні від користувача
# і передаватиме список чисел в обробник (хендлер)
class NumbersInMessage(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict[str, list[int]]:
        numbers = []
        # Розбиваємо повідомлення на окремі слова за пробілами, нормалізуємо кожне слово,
        # видаляючи зайві розділові знаки і невидимі символи, перевіряємо, що в таких словах
        # є лише цифри, перетворюємо на цілі числа та додаємо їх до списку
        for word in message.text.split():
            # normalized_word = word.replace('.', '').replace(',', '').strip()
            normalized_word = word.strip(".,")
            if normalized_word.isdigit():
                numbers.append(int(normalized_word))
        # Якщо в списку є числа, повертаємо список за ключем 'numbers':
        if numbers:
            return {'numbers': numbers}
        return False

# Цей обробник буде запускатися, якщо повідомлення користувача
# починається фразою "знайди числа" і містить числа
@dp.message(Text(startswith='знайди числа', ignore_case=True),
            NumbersInMessage())
# Крім об'єкта типу Message, приймаємо список чисел з фільтра
async def process_if_numbers(message: Message, numbers: list[int]):
    await message.answer(
            text=f'Знайшов: {", ".join(str(num) for num in numbers)}')


# Цей обробник буде запускатися, якщо повідомлення користувача
# починається фразою "знайди числа", але не містить чисел
@dp.message(Text(startswith='знайди числа', ignore_case=True))
async def process_if_not_numbers(message: Message):
    await message.answer(
            text='Щось не знайшов :(')



dp.run_polling(bot)
