# Gpt4free Telegram-Bot

## Описание
Данный код представляет собой telegram-бота, использующего искусственный интеллект для генерации ответов на сообщения пользователей. 
Бот поддерживает удаление данных пользователя и обработку сообщений, а также предотвращает превышение лимита на количество символов в сообщении.

## Использование
1. Установите зависимости с помощью команды
```
pip install -r requirements.txt
```
2. Создайте файл `.env` и добавьте в него API токен своего telegram-бота в формате
```
API_TOKEN=ваш_токен
```
3. Запустите бота с помощью команды
```
python main.py
```

## Функционал
1. Бот реагирует на команду /start и отправляет приветственное сообщение.
2. Пользователь может отправлять любые сообщения боту, на которые он генерирует ответы.
3. При превышении лимита на количество символов в сообщении, бот отправляет предупреждение.
4. Бот автоматически очищает сообщения пользователя, если их количество превышает лимит.
5. Пользователь может запросить удаление своих данных с помощью кнопки "Очистить данные".
