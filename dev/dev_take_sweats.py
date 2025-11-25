from datetime import timedelta

from app.calendar.models import RegularEvent
from app.profile.models import Profile


def handle():
    profile = Profile.get()
    start = profile.now
    end = start + timedelta(minutes=15)
    regular_event = RegularEvent.get_object(name='Есть вкусняшки')
    regular_event.start(start_dt=start, end_dt=end)
