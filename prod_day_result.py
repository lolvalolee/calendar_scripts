from datetime import datetime

from app.habit.models import UserHabit
from app.calendar.models import Event

now = datetime.now()
# '❌'

event = Event.get_objects('/api/event/current/')
print(event)
habit, _ = UserHabit.get_objects()
for item in habit:
    results, _ = item.results()
    print(results)
