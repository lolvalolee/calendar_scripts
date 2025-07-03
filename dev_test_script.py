import sys

from app.notification.models import Message, NotificationTransport

sys.path.append('./')

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
                'type': 'habit_report',
                'result': 'completed',
                'qs': {'name': 'Eothyrox'}
            }
        },
    ]
}

Message.question(transport=NotificationTransport.desktop(), extra_data=extra_data)
