from datetime import datetime

from app.habit.models import UserHabit
from app.calendar.models import Event

now = datetime.now()
# '❌'

events, _ = Event.get_objects('/api/event/current/')
event = events[0]
print(event.start)

habit, _ = UserHabit.get_objects()
for item in habit:
    results, _ = item.results()
    print(results)
