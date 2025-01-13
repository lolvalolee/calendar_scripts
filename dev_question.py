import sys
from app.notification.models import Message, NotificationTransport

sys.path.append('./')

extra_data = {
    'title': 'Начать событие сон',
    'questions': [
        {
            'title': 'Нет',
            'action': {
                'type': 'delete_notification',
                'qs': {'name': 'Сон'}
            }
        },
        {
            'title': 'Да',
            'action': {
                'type': 'start_regular_event',
                'qs': {'name': 'Сон'}
            }
        },
    ]
}

Message.simple_message(transport=NotificationTransport.desktop(), extra_data={'title': f'запланировано на завтра с 10:00 до 10:45'})
