import os

from app.handler.constants import ACTION_CALL_HANDLER
from app.notification.models import Message, NotificationTransport
from utils.misc import get_handler_extra_data


def handle():
    # Message.simple_messagev2('test message', NotificationTransport.telegram())
    print(get_handler_extra_data())
    questions = [
        {
            'title': 'Кусь',
            'action': {
                'type': ACTION_CALL_HANDLER,
                'qs': {'name': 'test'},
                'handler_extra_data': {'i': '-'}
            }
        },
        {
            'title': 'Грызь!',
            'action': {
                'type': ACTION_CALL_HANDLER,
                'qs': {'name': 'test'},
                'handler_extra_data': {'i': '+'}
            }
        },
    ]

    extra_data = {
        'title': 'Кусь или грызь?',
        'questions': questions
    }

    Message.question(transport=NotificationTransport.telegram(), extra_data=extra_data)
