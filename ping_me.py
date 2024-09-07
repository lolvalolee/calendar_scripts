from datetime import datetime, timedelta, time

import os
import sys
from typing import List

from app.calendar.models import RegularEvent, Event
from app.profile.models import Profile

sys.path.append('./')


def calc_total(_events: List[Event]):
    _total = sum([e.duration_seconds for e in _events])
    _diff = _total - (60 * 60 * 8)
    return _total, _diff, abs(_diff) < allowed_diff, _diff < 0


os.environ.setdefault('TOKEN', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI2Mjc3ODU0LCJqdGkiOiIzOTgwNWQzYTFkOTI0YzZjODZhZDc4YTAwMWQ2ZTU5NSIsInVzZXJfaWQiOjF9.FrTijv92PJezMPszf5_sTXdZflI3SwbwfiWXKMt7hXE')
r = RegularEvent.get_object(1)
profile = Profile.get()

now = datetime.utcnow().astimezone()
prev = now - timedelta(days=1)
next_day = now + timedelta(days=1)

allowed_diff = 10 * 60
max_diff = 2 * 60 * 60

events = r.events(start_gte=prev, end_lte=now)
total, diff, out_of_allowed_range, increase = calc_total(r.events(start_gte=prev, end_lte=now))

next_events = r.events(start_gte=now, end_lte=next_day)
planned_events = r.planned_events()

next_total, *other = calc_total(next_events)

if not next_events:
    tz = profile.user_timezone
    dt = now.replace(tzinfo=tz)
    start = datetime.combine(dt.date(), time(23, 00), tzinfo=tz)

    end = start + timedelta(hours=8)
    start = getattr(start, '__add__' if diff > 0 else '__sub__')(timedelta(seconds=min(abs(diff), max_diff)))
    Event.create(start=start, end=end, title={'value': 'Сон'})
