import json
import os
import re
import sys
from datetime import datetime, timedelta

from app.calendar.models import Event, RegularEvent
from app.notification.constants import BUTTON_VARIANT_WARNING
from app.notification.models import Message, NotificationTransport
from app.profile.models import UserStatus
from handlers.constants import HABIT_ACTION_REPORT, VOICE_COMMAND_REGEXPS, ACTION_EVENT_START
from handlers.event_voice_command import start_event
from handlers.habit_voice_command import handle_habit_report

sys.path.append('./')

mood = json.loads(os.environ.get('handler_extra_data'))['mood']
_now = datetime.now()

if mood == 'Настроение: хорошее':
    Message.simple_messagev2(transport=NotificationTransport.telegram(),
                             title='Супер. Тогда кофе, небольшая разминка и завтрак.')
    RegularEvent.get_object(name='утренний кофе').start(start_dt=_now + timedelta(minutes=10))
print(mood, mood == 'Настроение: хорошее')

#
# statuses, _ = UserStatus.get_objects()
#
# questions = [
#     {
#         'title': item.name['value'],
#         'style': BUTTON_VARIANT_WARNING,
#         'action': {
#             'type': 'call_handler',
#             'qs': {'id': 11},
#             'handler_extra_data': {
#                 'mood': item.label
#             }
#         }
#     } for item in statuses
# ]
#
# extra_data = {
#     'title': 'Начать событие сон?',
#     'questions': questions
# }
# Message.question(transport=NotificationTransport.telegram(), extra_data=extra_data)
