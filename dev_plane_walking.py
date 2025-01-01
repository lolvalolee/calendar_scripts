import sys
from datetime import datetime, timedelta

from app.calendar.models import RegularEvent, Event

sys.path.append('./')

from app.profile.models import Profile


profile = Profile.get()
tz = profile.user_timezone
now = profile.now
now = now.replace(hour=7, minute=0, second=0, microsecond=0)
start = now + timedelta(days=1)
start = start.replace(hour=10)
end = start.replace(hour=10, minute=45)

# filter events
# if not event: create meal
regular_event = RegularEvent.get_object(name='Сон')
Event.create(regular_event=regular_event.id, start=start, end=end, title={'value': 'Сон'})


