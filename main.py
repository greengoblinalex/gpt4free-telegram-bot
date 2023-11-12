import json
import aiofiles
import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import g4f

from constants import (MAX_MESSAGES, START_PHRASE,
                       DATA_FILE, START_COMMAND,
                       FIRST_QUESTION, FIRST_ANSWER)

load_dotenv()

bot = Bot(token=os.getenv('API_TOKEN'))
dp = Dispatcher(bot)


async def save_to_json(filename, data):
    async with aiofiles.open(filename, 'w', encoding='utf-8') as file:
        await file.write(json.dumps(data, ensure_ascii=False))


async def load_from_json(filename):
    try:
        async with aiofiles.open(filename, 'r', encoding='utf-8') as file:
            data = await file.read()
            return json.loads(data)
    except FileNotFoundError:
        async with aiofiles.open(filename, 'w', encoding='utf-8') as file:
            await file.write('{}')
            return {}


def get_user_messages_list(user_id, users_messages):
    messages = []
    if user_id in users_messages:
        messages = users_messages[user_id]

    if len(messages) > MAX_MESSAGES:
        messages = messages[-MAX_MESSAGES:]

    if len(messages) == 0 or messages[0] != FIRST_QUESTION:
        messages.insert(0, FIRST_QUESTION)

    if len(messages) < 2 or messages[1] != FIRST_ANSWER:
        messages.insert(1, FIRST_ANSWER)

    return messages


async def ask_gpt(messages):
    return await g4f.ChatCompletion.create_async(
        model=g4f.models.gpt_35_turbo,
        messages=messages
    )


@dp.message_handler()
async def process_message(message: types.Message):
    if message.text.lower() == START_COMMAND:
        await message.answer(START_PHRASE)
    else:
        user_id = str(message.from_user.id)
        users_messages = await load_from_json(DATA_FILE)

        messages = get_user_messages_list(user_id, users_messages)

        messages.append(
            {
                'role': 'user',
                'content': message.text
            }
        )

        answer = await ask_gpt(messages)
        await message.answer(answer)

        messages.append({'role': 'assistant', 'content': answer})
        users_messages[user_id] = messages

        await save_to_json(DATA_FILE, users_messages)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)