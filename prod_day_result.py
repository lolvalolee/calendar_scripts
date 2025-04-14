from datetime import datetime
from zoneinfo import ZoneInfo

from app.notification.models import NotificationTransport, Message
from utils.logger import logger

from app.habit.models import UserHabit
from app.calendar.models import Event, RegularEvent
from app.profile.models import Profile

now = datetime.now()

profile = Profile.get()
tz = ZoneInfo(profile.timezone)
events, _ = Event.get_objects('/api/event/current/')

test_event = RegularEvent.get_object(name='new regular event')
current_test_event = test_event.current()

event = events[0]
regular_event_chill_title = 'Отдых'
regular_event_chill = RegularEvent.get_object(name=regular_event_chill_title)

regular_event_work_title = 'Calendar'
regular_event_work = RegularEvent.get_object(name=regular_event_work_title)


_now = datetime.now(tz)
diff = int((_now - event.start).total_seconds())

habit, _ = UserHabit.get_objects()
logger.info('HERE IS LOGGGG')

for item in habit:
    results, _ = item.results(record_date__gte=event.start, order_by='record_date')
    if len(results) < 3:
        exit(0)
    for i, habit_result in enumerate(results):
        try:
            duration = (results[i+2].record_date - habit_result.record_date).total_seconds()

            if duration > 1:
                regular_event_work.end_now()
                regular_event_chill.start_now()

                r = Message.simple_message(transport=NotificationTransport.telegram(),
                                           extra_data={'title': 'Начал отвлекаться. Отдохни немного.'})

                exit(0)

        except IndexError:
            exit(0)
