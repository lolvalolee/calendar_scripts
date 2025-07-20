import json
import os
import re
import sys

from app.profile.models import UserStatus
from handlers.constants import HABIT_ACTION_REPORT, VOICE_COMMAND_REGEXPS, ACTION_EVENT_START
from handlers.event_voice_command import start_event
from handlers.habit_voice_command import handle_habit_report

sys.path.append('./')

statuses, _ = UserStatus.get_objects()
print(statuses)
