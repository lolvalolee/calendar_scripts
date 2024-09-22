from datetime import datetime, timedelta, time

import sys
from typing import List

from app.calendar.models import RegularEvent, Event
from app.notification.models import Message
from app.profile.models import Profile

sys.path.append('./')


r = Message.create()
print('******')
print(r)
print(r)