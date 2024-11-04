import os
import sys

from openai import OpenAI

from app.notification.models import Message, NotificationTransport


sys.path.append('./')
print('object_id : ')
print(os.environ["object_id"])