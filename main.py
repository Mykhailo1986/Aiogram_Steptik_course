from aiogram import Bot, Dispatcher
from aiogram.filters import Command, Text
from aiogram.types import Message
from aiogram.types import ContentType
from aiogram import F
import pprint
from config import
from functions import users, get_random_number

# Замість BOT TOKEN HERE потрібно вставити токен вашого бота, отриманого від @BotFather
API_TOKEN: str = TOKEN

# Створюємо об'єкти бота і диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

# кількість спроб
ATTEMPTS: int = 5


# Цей хендлер буде викликаний на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer(
        "Привіт! \n Давайте грати в гру «Вгадай число»? \n"
        " Для отримання правил гри і список доступних команд"
        " відправ команду /help"
    )
    if message.from_user.id not in users:
        users[message.from_user.id] = {
            "in_game": False,
            "secret_number": None,
            "attempts": None,
            "total_games": 0,
            "wins": 0,
        }


# Цей хендлер буде викликаний на команду "/help"
@dp.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await message.answer(
        "Правила гри:\n\nЯ загадую число від 1 до 100, "
        f"а вам потрібно його відгадати.\nУ вас є {ATTEMPTS} "
        "спробуй\n\nДоступні команди:\n/help - правила "
        "гри та список команд\n/cancel - вийти з гри\n"
        "/stat - переглянути статистику\n\nДавай зіграємо?"
    )


# TODO: не зрозумів чому використовують функцію старт 2 рази
# Этот хэндлер будет срабатывать на команду "/stat"
@dp.message(Command(commands=["stat"]))
async def process_stat_command(message: Message):
    await message.answer(
        f'Усього ігр зіграно: {users[message.from_user.id]["total_games"]}\n'
        f'З них виграно: {users[message.from_user.id]["wins"]}'
    )

# Цей хендлер буде викликаний на команду  "/cancel"
@dp.message(Command(commands=["cancel"]))
async def process_cancel_command(message: Message):
    if users[message.from_user.id]["in_game"]:
        await message.answer(
            "Ви вийшли з гри. Якщо захочете зіграти " "знову - повідомте про це."
        )
        users[message.from_user.id]["in_game"] = False
    else:
        await message.answer("Ми ж зараз не граємо. Можливо, зіграємо одну гру?")


# Цей хендлер буде викликаний при згоді зіграти у гру
@dp.message(
    Text(
        text=[
            "Так",
            "Впевнено",
            "Звичайно",
            "Звістно",
            "Гайда",
            "Давай",
            "Розпочнемо",
            "Починаймо",
            "Пограємо",
            "Зіграємо",
            "Розважимось",
            "Бажаю",
            "Гра",
            "Розвага",
            "Хочю",
            "Забава",
            "Грати",
            "Розігрувати",
            "Брати участь у грі",
            "Бажаю грати",
            "Мені хочеться грати",
            "Хотів би зіграти",
        ],
        ignore_case=True,
    )
)
async def process_positive_answer(message: Message):
    if not users[message.from_user.id]["in_game"]:
        await message.answer(
            "Ура!\n\nЯ загадав число від 1 до 100, " "спробуй вгадати!"
        )
        users[message.from_user.id]["in_game"] = True
        users[message.from_user.id]["secret_number"] = get_random_number()
        users[message.from_user.id]["attempts"] = ATTEMPTS
    else:
        await message.answer(
            "Поки ми граємо в гру, я можу реагувати лише на числа від 1 до 100 "
            "та команди /cancel і /stat."
        )


# Этот хэндлер будет срабатывать на отказ пользователя сыграть в игру
@dp.message(
    Text(text=["Нет", "Ні", "Не хочу", "Не буду"], ignore_case=True)
)  # ignore_case=True - игнорирование регистра,
async def process_negative_answer(message: Message):
    if not users[message.from_user.id]["in_game"]:
        await message.answer(
            "Шкода :\n\nЯкщо захочете зіграти - просто " "напишіть про це"
        )
    else:
        await message.answer(
            "Ми ж зараз граємо разом. Надсилайте, " "будь ласка, числа від 1 до 100"
        )


# Цей хендлер буде викликано при вводі цислф вфд 1  до 100
@dp.message(lambda numb: numb.text.isdigit() and 0 < int(numb.text) < 101)
async def process_numbers_answer(message: Message):
    if users[message.from_user.id]["in_game"]:
        if int(message.text) == users[message.from_user.id]["secret_number"]:
            await message.answer("Ура!!! Вгадали число!\n\n" "Може, ще зіграємо?")
            users[message.from_user.id]["in_game"] = False
            users[message.from_user.id]["total_games"] += 1
            users[message.from_user.id]["wins"] += 1
        elif int(message.text) > users[message.from_user.id]["secret_number"]:
            await message.answer("загадане число меньше")
            users[message.from_user.id]["attempts"] -= 1
        elif int(message.text) < users[message.from_user.id]["secret_number"]:
            await message.answer("Загадане число більше")
            users[message.from_user.id]["attempts"] -= 1
        if users[message.from_user.id]["attempts"] == 0:
            await message.answer(
                "На жаль, у вас більше не залишилося спроб. Ви програли :(\n\nМоє число "
                f'було {users[message.from_user.id]["secret_number"]}\n\nДавайте зіграємо ще раз?'
            )
            users[message.from_user.id]["in_game"] = False
            users[message.from_user.id]["total_games"] += 1
    else:
        await message.answer("Мы еще не играем. Хотите сыграть?")


# Цей хендлер буде викликаний на всі інші повідомлення
@dp.message()
async def process_other_text_answers(message: Message):
    if users[message.from_user.id]["in_game"]:
        await message.answer(
            "Ми ж зараз граємо. Будь ласка, " "надсилайте числа від 1 до 100"
        )
    else:
        await message.answer(
            "Я досить обмежений бот, давайте " "просто зіграємо в гру?"
        )


if __name__ == "__main__":
    dp.run_polling(bot)
#