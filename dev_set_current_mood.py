import json
import os
import re
import sys

from app.habit.constants import RESULT_COMPLETED, RESULT_FAILED
from app.habit.models import UserHabit
from app.notification.models import Message, NotificationTransport

sys.path.append('./')

from app.profile.models import UserStatus

import json
import os
import re
import sys

HABIT_ACTION_REPORT = 'отметь'

_habit_result_mapping = {
    RESULT_COMPLETED: ['выполнен',],
    RESULT_FAILED: ['провал',]
}
habit_result_mapping = {}
[habit_result_mapping.update({_value: key for _value in value}) for key, value in _habit_result_mapping.items()]

regexps = [
    f'^(?P<action>{HABIT_ACTION_REPORT}) привычку (?P<habit_name>.+) (?P<result>{"|".join(habit_result_mapping.keys())})',
    r'^((?P<action>начни|закончи) (?P<regular>регулярное )?событие (?P<event_name>.+))'
]

_habit_mapping = {
    'задротил': ['затратил', ]
}

_habit_result_mapping = {
    RESULT_COMPLETED: ['выполнен',],
    RESULT_FAILED: ['провал',]
}

habit_mapping = {}
[habit_mapping.update({_value: key for _value in value}) for key, value in _habit_mapping.items()]
habit_mapping.update({key: key for key in _habit_mapping.keys()})

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
        if not match:
            Message.simple_message(transport=NotificationTransport.telegram(),
                                   extra_data={'title': f'Команду невозможно обработать: {text}'})

    def handle_habit_report(self, *args, **options):
        habit_name = self.match.group('habit_name').lower()
        habit_name = habit_mapping.get(habit_name, habit_name)
        try:
            habit = UserHabit.get_object(name=habit_name)
            try:
                result = habit_result_mapping[self.match.group('result').lower()]
            except AttributeError:
                result = RESULT_COMPLETED
            habit.report(result)
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
