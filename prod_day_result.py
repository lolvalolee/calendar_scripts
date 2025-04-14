from datetime import datetime
from zoneinfo import ZoneInfo

from app.habit.models import UserHabit
from app.calendar.models import Event, RegularEvent
from app.profile.models import Profile

now = datetime.now()
# '❌'

profile = Profile.get()
tz = ZoneInfo(profile.timezone)
events, _ = Event.get_objects('/api/event/current/')

test_event = RegularEvent.get_object(name='new regular event')
current_test_event = test_event.current()
print(current_test_event)
exit(0)
event = events[0]
event_chill = 'Отдых'
event_work = 'Calendar'
_now = datetime.now(tz)
diff = int((_now - event.start).total_seconds())
print(diff)

habit, _ = UserHabit.get_objects(record_date__lte=event.start)

for item in habit:
    results, _ = item.results()
    print(results)
    if len(results) < 3:
        exit(0)
    for i, habit_result in enumerate(results):
        try:
            duration = (results[i+2].record_date - habit_result.record_date).total_seconds()
            if duration > (60 * 5):
                print('sevent should be stopped')
                _calendar, _ = Event.get_objects(name=event_work)[0]
                _calendar._call_action()
                # _chill, _ = Event.get_objects(name=event_chill)[0]
                # _calendar.end_now()

        except IndexError:
            exit(0)
