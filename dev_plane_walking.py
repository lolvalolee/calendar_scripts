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
end = now + timedelta(days=2)

# filter events
# if not event: create meal
events, count = RegularEvent.get_object(name='Сон')


