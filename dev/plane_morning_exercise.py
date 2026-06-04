from app.handler.constants import ACTION_CALL_HANDLER
from app.training.models import UserExercise, UserTraining
from app.notification.models import Message, NotificationTransport

from utils.misc import get_handler_extra_data


ACTION_INCREASE = 1
ACTION_SKIP = 2
ACTION_SKIP_AND_PLANE = 3
ACTION_FORGET = 4


def create_question(exercise):
    questions = [
        {
            'title': f"Увеличить количество",
            'action': {
                'type': ACTION_CALL_HANDLER,
                'qs': {'name': 'test1'},
                'handler_extra_data': {'i': ACTION_INCREASE, 'a': ACTION_INCREASE}
            }
        },
        {
            'title': f"Пропустить",
            'action': {
                'type': ACTION_CALL_HANDLER,
                'qs': {'name': 'test1'},
                'handler_extra_data': {'i': exercise.id, 'a': ACTION_SKIP}
            }
        },
        {
            'title': f"",
            'action': {
                'type': ACTION_CALL_HANDLER,
                'qs': {'name': 'test1'},
                'handler_extra_data': {'i': exercise.id, 'a': ACTION_SKIP}
            }
        },
        {
            'title': f"Пропустить",
            'action': {
                'type': ACTION_CALL_HANDLER,
                'qs': {'name': 'test1'},
                'handler_extra_data': {'i': exercise.id, 'a': ACTION_SKIP}
            }
        }
    ]

    extra_data = {
        'title': 'Предметы склада',
        'questions': questions
    }

    Message.question(transport=NotificationTransport.telegram(), extra_data=extra_data)


def handle():
    print('**********')
    data = get_handler_extra_data()
    print(get_handler_extra_data())

    exercises = list(UserExercise.get_objects(extra_data__count=5))
    # print(UserTraining.create(user_training_exercises=[
    #     {'user_exercise': item.id, 'count': 1} for item in exercises
    # ]))

    n = data.get('n', 0)

    try:
        create_question(exercises[n])
    except IndexError:
        pass
