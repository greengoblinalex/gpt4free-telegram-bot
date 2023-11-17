import json
import aiofiles

import tiktoken


def get_num_tokens_from_string(string: str) -> int:
    encoding = tiktoken.encoding_for_model('gpt-3.5-turbo')
    return len(encoding.encode(string))


async def save_to_json(filename: str, data):
    async with aiofiles.open(filename, 'w', encoding='utf-8') as file:
        await file.write(json.dumps(data, ensure_ascii=False))


async def load_from_json(filename: str):
    try:
        async with aiofiles.open(filename, 'r', encoding='utf-8') as file:
            data = await file.read()
            return json.loads(data)
    except FileNotFoundError:
        async with aiofiles.open(filename, 'w', encoding='utf-8') as file:
            await file.write('{}')
            return {}
