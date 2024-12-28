from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import asyncio

bot = Bot(token='')
dp = Dispatcher()


@dp.message()
async def start_message(message: Message):
        await message.answer('Введите команду /start, чтобы начать общение.')


@dp.message(Command('/start'))
async def all_messages(message: Message):
        await message.answer('Привет! Я бот помогающий твоему здоровью.')
        print('Привет! Я бот помогающий твоему здоровью.')


async def main():
        await dp.start_polling(bot)


asyncio.run(main())
