import g4f

from constants import MAX_MESSAGES


def ask_gpt(messages):
    return g4f.ChatCompletion.create(
        model=g4f.models.gpt_35_turbo,
        messages=messages
    )


def main():
    messages = []
    while True:
        if len(messages) > MAX_MESSAGES:
            messages = messages[-MAX_MESSAGES:]

        messages.append(
            {
                'role': 'user',
                'content': input()
            }
        )

        answer = ask_gpt(messages)
        print(f'\nChatGPT: {answer}\n')
        messages.append(
            {
                'role': 'assistant',
                'content': answer
            }
        )
        print(messages)


if __name__ == '__main__':
    main()
