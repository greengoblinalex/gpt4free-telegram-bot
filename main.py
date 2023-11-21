import os
from typing import List

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import g4f

from utils import (save_to_json, load_from_json,
                   get_num_tokens_from_string)
from constants import (DATA_FILE, START_COMMAND,
                       CLEAR_DATA_BTN_TEXT,
                       MAX_TOKENS, START_PROMPT,
                       START_PHRASE, PLS_WAIT_PHRASE,
                       ERROR_PHRASE, CLEAR_DATA_PHRASE)

load_dotenv()

bot = Bot(token=os.getenv('API_TOKEN'))
dp = Dispatcher(bot)

main_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
main_keyboard.add(CLEAR_DATA_BTN_TEXT)
empty_keyboard = types.ReplyKeyboardRemove()


def get_messages_with_start_prompt(messages: List) -> List:
    if len(messages) == 0:
        messages = START_PROMPT
    return messages


def get_num_tokens_from_user_messages(messages: List) -> int:
    tokens = 0
    for message in messages:
        tokens += message.get('tokens')
    return tokens


def get_cleared_messages(messages: List,
                         current_num_tokens: int) -> List:
    messages_to_delete = []
    tokens_of_messages_to_delete = 0

    for i in range(len(START_PROMPT), len(messages)):
        if current_num_tokens - tokens_of_messages_to_delete < MAX_TOKENS:
            break

        tokens_of_messages_to_delete += messages[i]['tokens']
        messages_to_delete.append(messages[i])

    return [i for i in messages if i not in messages_to_delete]


async def get_gpt_answer(messages: List) -> str:
    return await g4f.ChatCompletion.create_async(
        model=g4f.models.gpt_35_turbo_16k_0613,
        messages=messages
    )


@dp.message_handler(text=CLEAR_DATA_BTN_TEXT)
async def clear_data(message: types.Message):
    user_id = str(message.from_user.id)
    users_messages = await load_from_json(DATA_FILE)

    if user_id in users_messages:
        users_messages[user_id] = []
        await save_to_json(DATA_FILE, users_messages)

    await message.answer(CLEAR_DATA_PHRASE,
                         reply_markup=empty_keyboard)


@dp.message_handler()
async def process_message(message: types.Message):
    if message.text.lower() == START_COMMAND:
        await message.answer(START_PHRASE)
    else:
        user_id = str(message.from_user.id)
        users_messages = await load_from_json(DATA_FILE)
        messages: List = get_messages_with_start_prompt(
            users_messages.get(user_id) or [])

        num_tokens_from_message = get_num_tokens_from_string(message.text)
        if num_tokens_from_message > MAX_TOKENS:
            await message.answer(ERROR_PHRASE)
            return

        current_num_tokens = (
            get_num_tokens_from_user_messages(messages) +
            num_tokens_from_message
        )

        if current_num_tokens > MAX_TOKENS:
            messages = get_cleared_messages(messages, current_num_tokens)

        wait_message = await message.answer(PLS_WAIT_PHRASE)

        messages.append({'role': 'user', 'content': message.text,
                        'tokens': num_tokens_from_message})

        answer = await get_gpt_answer(messages)
        await bot.delete_message(message.chat.id, wait_message.message_id)
        await message.answer(answer, reply_markup=main_keyboard)

        messages.append({'role': 'assistant', 'content': answer,
                        'tokens': get_num_tokens_from_string(answer)})

        users_messages[user_id] = messages
        await save_to_json(DATA_FILE, users_messages)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
