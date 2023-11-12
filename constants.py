MAX_MESSAGES = 20

DATA_FILE = 'data.json'

START_COMMAND = '/start'
START_PHRASE = 'Привет! Я ChatGPT-бот. Напиши свой вопрос, а я постараюсь ответить на него'

FIRST_QUESTION = {
    "role": "user",
    "content": "Отвечай только на русском, даже если я пишу на другом языке, если не попрошу ответ на другом языке."
}
FIRST_ANSWER = {
    "role": "assistant",
    "content": "Конечно, я буду отвечать только на русском языке, если вы не попросите ответить на другом языке."
}
