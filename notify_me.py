from datetime import datetime, timedelta, time

import sys
from typing import List

from app.calendar.models import RegularEvent, Event
from app.notification.models import Message, NotificationTransport
from app.profile.models import Profile

sys.path.append('./')

desktop = NotificationTransport.desktop()
print(desktop.id)


r = Message.simple_message(transport=desktop)
print('******')
print(r)
