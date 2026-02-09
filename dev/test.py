from app.handler.constants import ACTION_CALL_HANDLER
from app.notification.models import Message, NotificationTransport
from utils.misc import get_handler_extra_data


def handle():
    print(get_handler_extra_data())
    meal = ['opti meal', 'purina']
    questions = [
        {
            'title': 'Кусь',
            'action': {
                'type': ACTION_CALL_HANDLER,
                'qs': {'name': 'test'},
                'handler_extra_data': {'i': item}
            }
        }
        for item in meal
    ]

    extra_data = {
        'title': 'Чем сегодня задабривал зверя?',
        'questions': questions
    }

    Message.question(transport=NotificationTransport.telegram(), extra_data=extra_data)
