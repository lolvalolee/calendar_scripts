import sys

from app.notification.models import Message, NotificationTransport
from app.profile.models import UserStatus

sys.path.append('./')

statuses, _ = UserStatus.get_objects()

questions = [
    {
        'title': item.label,
        'action': {
            'type': 'call_handler',
            'qs': {'id': 11},
            'handler_extra_data': {
                'mood': item.label
            }
        }
    } for item in statuses
]

extra_data = {
    'title': 'Александр, как настроение с утра?',
    'questions': questions
}

Message.question(transport=NotificationTransport.desktop(), extra_data=extra_data)
