from app.handler.constants import ACTION_CALL_HANDLER
from app.training.models import UserExercise, UserTraining
from app.notification.models import Message, NotificationTransport

from utils.misc import get_handler_extra_data


ACTION_ACCEPT = 1
ACTION_SKIP = 2
ACTION_SKIP_AND_PLANE = 3
ACTION_FORGET = 4
ACTION_SET_TIME = 5

#start?
    #yes!
        #when?
            #now!
            #15!
            #30!
            #45!
            #60!
    #no!


def create_question():
    questions = [
        # {
        #     'title': f"Увеличить количество",
        #     'action': {
        #         'type': ACTION_CALL_HANDLER,
        #         'qs': {'name': 'test1'},
        #         'handler_extra_data': {'i': ACTION_INCREASE, 'a': ACTION_INCREASE}
        #     }
        # },
        {
            'title': f"Нет",
            # 'action': {
            #     'type': ACTION_CALL_HANDLER,
            #     'qs': {'name': 'test1'},
            #     'handler_extra_data': {'i': exercise.id, 'a': ACTION_SKIP}
            # }
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


def set_training_time(n=None):
    options = [item for item in range(0, 60, 10)]

    questions = [
        {
            'title': f"{item if item else 'now'}",
            'action': {
                'type': ACTION_CALL_HANDLER,
                'qs': {'name': 'test1'},
                'handler_extra_data': {'a': ACTION_ACCEPT, 'i': item}
            }
        } for item in options
    ]
    Message.question_v2('Через сколько начать?', questions, transport=NotificationTransport.telegram())


def handle():
    data = get_handler_extra_data()
    n = data.get('n', 0)
    action = data.get('a')

    if not action:
        create_question()

    if action == ACTION_ACCEPT:
        set_training_time()

    #
    # print(get_handler_extra_data())
    #
    # exercises = list(UserExercise.get_objects(extra_data__count=5))
    # # print(UserTraining.create(user_training_exercises=[
    # #     {'user_exercise': item.id, 'count': 1} for item in exercises
    # # ]))
    # if action:
    #     pass
    #
    #
    #
    # n = data.get('n', 0)
    #
    # try:
    #     create_question(exercises[n])
    # except IndexError:
    #     pass
