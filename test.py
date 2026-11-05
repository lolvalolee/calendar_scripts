"""Тестовий хендлер: питає, що зробити з предметом склада.

Бекенд викликає ``handle()`` і передає параметри через ``handler_extra_data``.
Два виклики одного скрипта:

* **старт** — параметрів немає, беремо предмет за індексом ``n`` (типово 0)
  і шлемо питання з кнопками;
* **відповідь** — приходить від натиснутої кнопки: ``i`` — id предмета,
  ``a`` — код дії (``ACTION_INCREASE`` / ``ACTION_SKIP`` / …).

Моделі самі ходять на сервер — ні клієнта, ні налаштувань у скрипті немає.
"""

import logging

from calendar_scripts import get_handler_extra_data
from calendar_scripts.models import Exercise, Message, NotificationTransport

#: Дія правила ``call_handler``: натиск на кнопку викликає цей же скрипт.
ACTION_CALL_HANDLER = "call_handler"

ACTION_INCREASE = 1
ACTION_SKIP = 2
ACTION_SKIP_AND_PLANE = 3
ACTION_FORGET = 4

#: Назва цього скрипта — з нею бекенд викликає його по кнопці.
HANDLER_NAME = "test"

logger = logging.getLogger(__name__)


def create_question(exercise: Exercise) -> None:
    """Надсилає в телеграм питання з кнопками для одного предмета."""
    questions = [
        {
            "title": "Увеличить количество",
            "action": {
                "type": ACTION_CALL_HANDLER,
                "qs": {"name": HANDLER_NAME},
                "handler_extra_data": {"i": exercise.id, "a": ACTION_INCREASE},
            },
        },
        {
            "title": "Пропустить",
            "action": {
                "type": ACTION_CALL_HANDLER,
                "qs": {"name": HANDLER_NAME},
                "handler_extra_data": {"i": exercise.id, "a": ACTION_SKIP},
            },
        },
        {
            "title": "Отменить на сегодня",
            "action": {
                "type": ACTION_CALL_HANDLER,
                "qs": {"name": HANDLER_NAME},
                "handler_extra_data": {"i": exercise.id, "a": ACTION_SKIP},
            },
        },
    ]

    Message.question("Предметы склада", questions, NotificationTransport.telegram())


def handle() -> None:
    data = get_handler_extra_data()
    logger.info("handler_extra_data=%s", data)

    # Пришла відповідь на кнопку: id предмета є прямо в параметрах.
    if (exercise_id := data.get("i")) is not None:
        exercise = Exercise.get(exercise_id)
        logger.info("обрано дію %s для предмета %s", data.get("a"), exercise.id)
        return

    # Старт: предмет за індексом ``n``; немає такого — просто виходимо.
    n = data.get("n", 0)
    try:
        exercise = Exercise.objects()[n]
    except IndexError:
        logger.info("предметів менше, ніж %s", n + 1)
        return

    create_question(exercise)
