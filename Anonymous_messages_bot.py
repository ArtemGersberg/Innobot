from aiogram import Bot, Dispatcher, executor, types
import logging
from aiogram.types import Message
from TOKENenvAnonymous import TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from random import choice


logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)

waiting_users_id = set()
chatting_users_id = set()




@dp.message_handler(commands=["start", "help"], state='*')
async def start_command_handler(message: Message, state: FSMContext):
    await message.reply(f"Hi!\nI'm anonymous chat!\nTell me your name.")
    await state.set_state("q1")




@dp.message_handler(state="q1")
async def process_name(message: Message, state: FSMContext):
    name = message.text
    await state.update_data({"name": name})
    await state.set_state("q2")
    await message.answer("Tell me your age)")


@dp.message_handler(state="q2")
async def process_age(message: Message, state: FSMContext):
    age = message.text
    if age.isdigit() and int(age) >= 18:
        age = int(age)
        await state.update_data({"age": int(age)})
        await state.set_state("waiting")
        waiting_users_id.add(message.from_user.id)
        data = await state.get_data()
        if age % 10 == 1 and not age % 100 == 11 and age % 10 == 2 or age % 10 == 3 or age % 10 == 4 and not age % 100 == 12 and not age % 100 == 13 and not age % 100 == 14:
            await bot.send_message(chat_id=message.chat.id, text=f'Hi {data["name"]}, {data["age"]} year')
            year = "year"
            await state.update_data({"year": year})
            await message.answer("Now I'm an anonymous chat")
            await state.update_data({"year": year})
        else:
            await bot.send_message(chat_id=message.chat.id, text=f'Hi {data["name"]}, {data["age"]} years')
            year = 'years'
            await state.update_data({"year": year})
            await message.answer("Now I'm an anonymous chat")
    elif age.isdigit() and int(age) < 18:
        await message.answer("You're too young")
    else:
        await message.answer("This is not a number, try another time")


@dp.message_handler(commands=['find', 'next'], state='waiting')
async def waiting(message: Message, state: FSMContext):
    current_user = message.from_user.id
    waiting_users_id.add(current_user)
    await bot.send_message(message.chat.id, text="Looking for a new interlocutor...")
    target = await get_target(message, waiting_users_id, chatting_users_id)
    if target:
        target_state: FSMContext = dp.current_state(chat=target, user=target)
        await state.update_data({"target": target})
        await target_state.update_data({"target": current_user})
        await state.set_state('chatting')
        await target_state.set_state('chatting')
        chatting_users_id.add(current_user)
        chatting_users_id.add(target)

        current_user_data = await state.get_data()
        target_data = await target_state.get_data()
        current_user_name = current_user_data['name']
        target_name = target_data['name']

        await bot.send_message(current_user, f"Now you're talking to {target_name} ")
        await bot.send_message(target, f"Now you're talking to {current_user_name} ")


@dp.message_handler(state='chatting')
async def chat(message: Message, state: FSMContext):
    user_data = await state.get_data()
    user_name = user_data['name']
    target = user_data['target']

    await bot.send_message(target, text=f"<{user_name}>: {message.text}")


@dp.message_handler(commands=['next'], state='chatting')
async def next_chat(message, state):
    await state.set_state('waiting')


@dp.callback_query_handler(lambda callback: callback.data == 'i1')
async def procces_callback_button1(callback_query):
    await bot.answer_callback_query(callback_query.id, 'Callback Answered')
    await bot.send_message(callback_query.from_user.id, 'Up')


@dp.callback_query_handler(lambda callback: callback.data == 'i2')
async def procces_callback_button2(callback_query):
    await bot.answer_callback_query(callback_query.id, 'Callback Answered')
    await bot.send_message(callback_query.from_user.id, 'Down')


async def get_target(message, users: set[int], already_connected_users: set[int]) -> int:
    current_user = message.from_user.id
    user_targets = set(users) - already_connected_users - {current_user, }
    user_targets = list(user_targets)
    if user_targets:
        user_target = choice(user_targets)
        users.remove(user_target)
        return user_target
    else:
        await message.answer('Are you alone here')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)