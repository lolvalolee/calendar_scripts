from datetime import datetime

from app.habit.models import UserHabit
from app.calendar.models import Event

now = datetime.now()
# '❌'

events, _ = Event.get_objects('/api/event/current/')
event = events[0]
_now = datetime.now()
diff = (_now - event.start).total_seconds()

habit, _ = UserHabit.get_objects(record_date__lte=event.start)

for item in habit:
    results, _ = item.results()
    print(results)
