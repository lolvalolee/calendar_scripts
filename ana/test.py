from app.handler.constants import ACTION_CALL_HANDLER
from app.notification.models import Message, NotificationTransport


def handle():
    # Message.simple_messagev2('test message', NotificationTransport.telegram())

    questions = [
        {
            'title': 'Кусь',
            'action': {
                'type': ACTION_CALL_HANDLER,
                'qs': {'name': 'test_handler_ana'},
                'handler_extra_data': {'i': '-'}
            }
        },
        {
            'title': 'Грызь!',
            'action': {
                'type': ACTION_CALL_HANDLER,
                'qs': {'name': 'test_handler_ana'},
                'handler_extra_data': {'i': '+'}
            }
        },
    ]

    extra_data = {
        'title': 'Кусь или грызь?',
        'questions': questions
    }

    Message.question(transport=NotificationTransport.desktop(), extra_data=extra_data)
