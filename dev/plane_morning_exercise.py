from datetime import datetime, timedelta

from app.handler.constants import ACTION_CALL_HANDLER
from app.notification.models import Message, NotificationTransport
from app.calendar.models import RegularEvent
from app.training.models import UserTrainingExercise, UserExercise

from utils.misc import get_handler_extra_data


ACTION_ACCEPT = 1
ACTION_SKIP = 2
ACTION_SKIP_AND_PLANE = 3
ACTION_FORGET = 4
ACTION_SET_TIME = 5


def create_question():
    questions = [
        {
            'title': f"Нет",
        },
        {
            'title': f"Да",
            'action': {
                'type': ACTION_CALL_HANDLER,
                'qs': {'name': 'test1'},
                'handler_extra_data': {'a': ACTION_ACCEPT}
            }
        }
    ]

    extra_data = {
        'title': 'Будем тренироваться?',
        'questions': questions
    }

    Message.question(transport=NotificationTransport.telegram(), extra_data=extra_data)


def select_training_time(n=None):
    options = [item for item in range(0, 60, 10)]

    questions = [
        {
            'title': f"{item if item else 'now'}",
            'action': {
                'type': ACTION_CALL_HANDLER,
                'qs': {'name': 'test1'},
                'handler_extra_data': {'a': ACTION_SET_TIME, 'i': item}
            }
        } for item in options
    ]
    Message.question_v2('Через сколько начать?', questions, transport=NotificationTransport.telegram())


def plane_training(i):
    now = datetime.now()
    start = now + timedelta(minutes=i)

    regular_event = RegularEvent.get_object(name='завтрак')
    r = regular_event.create_event(title={'value': 'завтрак'}, start=start)

    exercises = list(UserExercise.get_objects(extra_data__morning=1))
    print(exercises)
    # if r.ok:
    #     Message.simple_messagev2('Запланировано!', NotificationTransport.telegram())


def handle():
    data = get_handler_extra_data()

    plane_training(1)

    return
    n = data.get('n', 0)
    i = data.get('i', 0)
    action = data.get('a')

    if not action:
        create_question()

    if action == ACTION_ACCEPT:
        select_training_time()

    if action == ACTION_SET_TIME:
        plane_training(i)
