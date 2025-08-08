from app.notification.constants import BUTTON_VARIANT_WARNING
from app.notification.models import Message, NotificationTransport
from app.profile.models import UserStatus


def handle():
    statuses, _ = UserStatus.get_objects()

    questions = [
        {
            'title': item.name['value'],
            'style': BUTTON_VARIANT_WARNING,
            'action': {
                'type': 'call_handler',
                'qs': {'name': 'set_current_mood'},
                'handler_extra_data': {
                    'mood': item.label
                }
            }
        } for item in statuses
    ]

    extra_data = {
        'title': 'Сань, какое настроение?',
        'questions': questions
    }

    Message.question(transport=NotificationTransport.telegram(), extra_data=extra_data)
