from datetime import datetime
from zoneinfo import ZoneInfo

from app.habit.models import UserHabit
from app.calendar.models import Event
from app.profile.models import Profile

now = datetime.now()
# '❌'

profile = Profile.get()
tz = ZoneInfo(profile.timezone)
now = datetime.now(tz)
events, _ = Event.get_objects('/api/event/current/')
event = events[0]
_now = datetime.now(tz)
diff = (_now - event.start).total_seconds()

habit, _ = UserHabit.get_objects(record_date__lte=event.start)

for item in habit:
    results, _ = item.results()
    print(results)
