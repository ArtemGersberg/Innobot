import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

logging.basicConfig(level=logging.INFO)

TOKEN = "6293237913:AAEi8V9plxPPdq2l3AIe4yDyshkReKO-S5I"

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

connected_users = []


@dp.message_handler(commands=['start', 'help'], state='*')
async def send_welcome(message: types.Message, state: FSMContext):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.answer("Hi!\nI'm EchoBot!\nPowered by aiogram.\nPlease, say your name")
    await state.set_state("q1")


@dp.message_handler(state="q1")
async def process_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data({"name": name})
    await state.set_state("q2")
    await message.answer("Say your age")


@dp.message_handler(state="q2")
async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    if age.isdigit():
        await state.update_data({"age": int(age)})
        await state.set_state("echo")
        await message.answer("Now I am echo-bot!")
        connected_users.append(message.from_user.id)
    else:
        data = await state.get_data()
        await message.answer(f"This is not a number, try another time {data['name']}")


@dp.message_handler(state="echo")
async def echo(message: Message):
    for user in connected_users:
        if message.from_user.id == user:
            continue
        await bot.send_message(user, message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
