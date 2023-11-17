MAX_TOKENS = 3072 - 45 - 40

DATA_FILE = 'data.json'

START_COMMAND = '/start'

START_PHRASE = 'Здравствуйте! Я ChatGPT-бот. Напишите свой вопрос, а я постараюсь ответить на него.'
PLS_WAIT_PHRASE = 'Пожалуйста, подождите немного, пока я думаю над ответом...'
ERROR_PHRASE = 'Слишком большое сообщение, пожалуйста, сократите его и отправьте еще раз.'

START_PROMPT = [
    {
        "role": "user",
        "content": "Отвечай только на русском, даже если я пишу на другом языке, если не попрошу ответ на другом языке.",
        "tokens": 45
    },
    {
        "role": "assistant",
        "content": "Конечно, я буду отвечать только на русском языке, если вы не попросите ответить на другом языке.",
        "tokens": 40
    }
]
