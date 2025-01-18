import sys

from app.notification.constants import BUTTON_VARIANT_SUCCESS, BUTTON_VARIANT_WARNING
from app.notification.models import Message, NotificationTransport

sys.path.append('./')

extra_data = {
    'title': 'Начать событие сон?',
    'questions': [
        {
            'title': 'Нет',
            'style': BUTTON_VARIANT_WARNING,
            'action': {
                'type': 'delete_notification',
                'qs': {'name': 'Сон'}
            }
        },
        {
            'title': 'Да',
            'style': BUTTON_VARIANT_SUCCESS,
            'action': {
                'type': 'start_regular_event',
                'qs': {'name': 'Сон'}
            }
        },
    ]
}

Message.question(transport=NotificationTransport.desktop(), extra_data=extra_data)
