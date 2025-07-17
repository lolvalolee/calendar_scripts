import json
import os
import re
import sys

from handlers.constants import HABIT_ACTION_REPORT, VOICE_COMMAND_REGEXPS
from handlers.habit_voice_command import handle_habit_report

sys.path.append('./')

from app.habit.constants import RESULT_COMPLETED, RESULT_FAILED
from app.notification.models import Message, NotificationTransport

# text = "отметь привычку Тренировка выполнена"
text = json.loads(os.environ.get('handler_extra_data'))['voice_command'].lower()


class CommandHandler:
    cmd = None
    match = None

    def __init__(self, cmd):
        self.cmd = cmd

        for regex in VOICE_COMMAND_REGEXPS:
            match = re.match(regex, text)
            if match:
                self.match = match
                break
        if not match:
            Message.simple_message(transport=NotificationTransport.telegram(),
                                   extra_data={'title': f'Команду невозможно обработать: {text}'})
            exit(0)

    def handle(self, *args, **options):
        groupdict = self.match.groupdict()
        action = groupdict['action']

        handlers_map = {
            HABIT_ACTION_REPORT: handle_habit_report,
        }
        handlers_map[action](self.match)


cmd = CommandHandler(text)
cmd.handle()
