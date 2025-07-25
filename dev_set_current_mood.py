import json
import os
import re
import sys

from app.notification.constants import BUTTON_VARIANT_WARNING
from app.notification.models import Message, NotificationTransport
from app.profile.models import UserStatus
from handlers.constants import HABIT_ACTION_REPORT, VOICE_COMMAND_REGEXPS, ACTION_EVENT_START
from handlers.event_voice_command import start_event
from handlers.habit_voice_command import handle_habit_report

sys.path.append('./')

statuses, _ = UserStatus.get_objects()

questions = [
    {
        'title': item.name['value'],
        'style': BUTTON_VARIANT_WARNING,
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
    'title': 'Начать событие сон?',
    'questions': questions
}
Message.question(transport=NotificationTransport.telegram(), extra_data=extra_data)
