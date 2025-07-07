import json
import os
import sys

from app.notification.models import Message, NotificationTransport
from app.profile.models import UserStatus

sys.path.append('./')

statuses, _ = UserStatus.get_objects()

print(os.environ.get('handler_extra_data') == 'хорошее настроение')
data = json.loads(os.environ.get('handler_extra_data'))
print(data)
print(data['mood'])
print(data['mood'] == 'хорошее настроение')
