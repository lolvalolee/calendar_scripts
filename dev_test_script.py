import os
import sys

from app.notification.models import Message, NotificationTransport

sys.path.append('./')

print('param!')
print(os.environ.get('handler_extra_data'))

extra_data = {
    'title': 'Начать событие сон?',
    'questions': [
        {
            'title': 'Нет',
            'action': {
                'type': 'delete_notification',
                'qs': {'name': 'Сон'}
            }
        },
        {
            'title': 'Сьел!',
            'action': {
                'type': 'call_handler',
                'qs': {'id': 9},
                'handler_extra_data': {
                    'test_key': 'test_value'
                }
            }
        },
    ]
}

Message.question(transport=NotificationTransport.desktop(), extra_data=extra_data)
