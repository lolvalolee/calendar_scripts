import json
import os
import re
import sys

from app.habit.models import UserHabit
from app.notification.models import Message, NotificationTransport

sys.path.append('./')

from app.profile.models import UserStatus

import json
import os
import re
import sys

HABIT_ACTION_REPORT = 'отметь'

regexps = [
    f'^(?P<action>{HABIT_ACTION_REPORT}) привычку (?P<habit_name>.+) (?P<result>выполнена|отменена|провалена)',
    r'^((?P<action>начни|закончи) (?P<regular>регулярное )?событие (?P<event_name>.+))'
]

# text = "отметь привычку Тренировка выполнена"
text = json.loads(os.environ.get('handler_extra_data'))['voice_command'].lower()

class CommandHandler:
    cmd = None
    match = None

    def __init__(self, cmd):
        self.cmd = cmd

        for regex in regexps:
            match = re.match(regex, text)
            if match:
                self.match = match
                break

    def handle_habit_report(self, *args, **options):
        print('hey!')
        habit = UserHabit.get_object(name=self.match.group('habit_name').lower())

    def handle(self, *args, **options):
        groupdict = self.match.groupdict()
        action = groupdict['action']

        handlers_map = {
            HABIT_ACTION_REPORT: self.handle_habit_report,
        }
        handlers_map[action](*args, **options)

Message.simple_message(transport=   NotificationTransport.telegram(), extra_data={'title': f'Текст сообщения: {text}'})

cmd = CommandHandler(text)
cmd.handle()

