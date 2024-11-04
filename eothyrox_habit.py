import os
import sys

from openai import OpenAI

from app.habit.models import UserHabitRecord
from app.notification.models import Message, NotificationTransport


sys.path.append('./')
print('object_id : ')
print(os.environ["object_id"])
objects = UserHabitRecord.get_objects()
obj = UserHabitRecord.get_object(os.environ["object_id"])
print(objects)
print(obj)