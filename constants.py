DATA_FILE = 'data.json'

# Commands
START_COMMAND = '/start'

# Buttons
CLEAR_DATA_BTN_TEXT = 'Очистить контекст'

# Phrases
START_PHRASE = 'Здравствуйте! Я ChatGPT-бот. Напишите свой вопрос, а я постараюсь ответить на него.'
PLS_WAIT_PHRASE = 'Пожалуйста, подождите немного, пока я думаю над ответом...'
LIMIT_ERROR_PHRASE = 'Слишком большое сообщение, пожалуйста, сократите его и отправьте еще раз.'
CLEAR_DATA_PHRASE = 'Контекст очищен. Давайте начнем диалог с чистого листа. Чем я могу помочь?'

RUNTIME_ERROR_PHRASE = 'В данный момент не удалось обработать Ваш запрос, попробуйте очистить контекст и повторить попытку позже.'
EN_RUNTIME_ERROR_PHRASE = 'OpenAI API failed. Please try your prompt again.'

# g4f
MAX_TOKENS = 3072 - 45 - 40
MAX_MESSAGES = 4

START_PROMPT = (
    {
        'role': 'user',
        'content': 'Отвечай только на русском, даже если я пишу на другом языке, если не попрошу ответ на другом языке.',
        'tokens': 45
    },
    {
        'role': 'assistant',
        'content': 'Конечно, я буду отвечать только на русском языке, если вы не попросите ответить на другом языке.',
        'tokens': 40
    }
)
