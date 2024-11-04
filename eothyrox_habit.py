import os
import sys

from openai import OpenAI

from app.habit.models import UserHabitRecord, UserHabit
from app.notification.models import Message, NotificationTransport


sys.path.append('./')

objects = UserHabitRecord.get_objects()
user_habit_record = UserHabitRecord.get_object(os.environ["object_id"])
user_habit = UserHabit.get_object(user_habit_record.user_habit)

stock =
