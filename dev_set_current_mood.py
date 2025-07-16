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
    f'^(?P<action>{HABIT_ACTION_REPORT}) привычку (?P<habit_name>.+) (?P<result>выполнен|отмен|провал)',
    r'^((?P<action>начни|закончи) (?P<regular>регулярное )?событие (?P<event_name>.+))'
]

_habit_mapping = {
    'задротил': ['затратил', ]
}

habit_mapping = {}
[habit_mapping.update({_value: key for _value in value}) for key, value in _habit_mapping.items()]
habit_mapping.update({key: key for key in _habit_mapping.keys()})

# text = "отметь привычку Тренировка выполнена"
text = json.loads(os.environ.get('handler_extra_data'))['voice_command'].lower()
print('*************')
print(text)

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
        if not match:
            Message.simple_message(transport=NotificationTransport.telegram(),
                                   extra_data={'title': f'Команду невозможно обработать: {text}'})

    def handle_habit_report(self, *args, **options):
        print('hey!')
        habit_name = self.match.group('habit_name').lower()
        habit_name = habit_mapping[habit_name]
        try:

            habit = UserHabit.get_object(name=habit_name)
        except IndexError:
            Message.simple_message(transport=NotificationTransport.telegram(),
                                   extra_data={'title': f'Привычка : {habit_name} не найдена'})

    def handle(self, *args, **options):
        groupdict = self.match.groupdict()
        action = groupdict['action']

        handlers_map = {
            HABIT_ACTION_REPORT: self.handle_habit_report,
        }
        handlers_map[action](*args, **options)

Message.simple_message(transport=NotificationTransport.telegram(), extra_data={'title': f'Текст сообщения: {text}'})

cmd = CommandHandler(text)
cmd.handle()

