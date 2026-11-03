"""Проверка регулярного события N за последние два часа.

Если у события N за окно нет ни одной выполненной записи — просим DeepSeek
написать напоминание о пользе спорта и отправляем его как уведомление.
"""

import sys
from datetime import datetime, timedelta

import requests

from calendar_scripts.models import ApiKey, Message, NotificationTransport, RegularEvent


sys.path.append("./")

#: Id регулярного события, которое проверяем.
REGULAR_EVENT_ID = 1

#: Окно проверки — последние два часа.
WINDOW = timedelta(hours=2)

#: Название ключа, которым подписываем запрос к DeepSeek.
KEY_NAME = "deepseek"

desktop = NotificationTransport.desktop()


def events_last_two_hours(regular_event: RegularEvent) -> list:
    """Записи регулярного события за последние ``WINDOW``."""
    now = datetime.now().astimezone()
    return regular_event.events(start__gte=now - WINDOW, end__lte=now)


def sport_text(key: str) -> str:
    """Сгенерировать текст о пользе спорта через DeepSeek."""
    response = requests.post(
        "https://api.deepseek.com/chat/completions",
        headers={"Authorization": f"Bearer {key}"},
        json={
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": "Сегодня не было тренировки. Напиши короткое "
                    "сообщение (1-2 предложения) о том, что важно "
                    "заниматься спортом каждый день.",
                },
            ],
        },
        timeout=30,
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()


def handle() -> None:
    regular_event = RegularEvent.get_object(REGULAR_EVENT_ID)
    if events_last_two_hours(regular_event):
        return

    key = ApiKey.get_object(KEY_NAME)
    Message.simple_message(sport_text(key.key), desktop)


if __name__ == "__main__":
    handle()
