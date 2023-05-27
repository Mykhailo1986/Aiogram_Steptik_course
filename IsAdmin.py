from aiogram import Bot, Dispatcher
from aiogram.filters import BaseFilter
from aiogram.types import Message
from config import TOKEN
from typing import Any

# Замість BOT TOKEN HERE потрібно вставити токен вашого бота, отриманого від @BotFather
API_TOKEN: str = TOKEN

# Створюємо об'єкти бота і диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

# список адміністраторів
admin_ids: list[int] = []


# власний фільтр який перевіряє юзера на адміна
class IsAdmin(BaseFilter):
    def __init__(self, admin_ids: list[int]) -> None:
        super().__init__()
        self.admin_ids = admin_ids

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids



# Цей хєндлер буде відповідати на апдєйт від админа
@dp.message(IsAdmin(admin_ids))
async def answer_if_admins_update(message: Message):
    await message.answer(text='Ви адмін')


# Цей хєндлер буде відповідати на апдєйт не від админа
@dp.message()
async def answer_if_not_admins_update(message: Message):
    await message.answer(text='Ви не адмін')

dp.run_polling(bot)
