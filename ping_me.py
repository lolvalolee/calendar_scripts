from datetime import datetime, timedelta, time

import sys
from typing import List

from app.calendar.models import RegularEvent, Event
from app.profile.models import Profile

from utils.models import ObjectsResponse
sys.path.append('./')
c = ObjectsResponse([1,2], 2)
for item in c:
    print(item)