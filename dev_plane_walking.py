import sys
from datetime import datetime, timedelta

from app.calendar.models import RegularEvent, Event

sys.path.append('./')

from app.profile.models import Profile


profile = Profile.get()
tz = profile.user_timezone
now = profile.now
now = now.replace(hour=7, minute=0, second=0, microsecond=0)

walking = 'Ходьба на беговой'
walking_start = now + timedelta(days=1)
walking_start = walking_start.replace(hour=10)
walking_end = walking_start.replace(hour=10, minute=45)

# filter events
# if not event: create meal
regular_event = RegularEvent.get_object(name=walking)
Event.create(regular_event=regular_event.id, start=walking_start, end=walking_end, title={'value': walking})


