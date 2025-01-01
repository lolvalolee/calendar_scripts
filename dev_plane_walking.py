import sys
from datetime import timedelta

from app.calendar.models import RegularEvent, Event
from app.notification.models import Message, NotificationTransport

sys.path.append('./')

from app.profile.models import Profile


profile = Profile.get()
tz = profile.user_timezone
now = profile.now
now = now.replace(hour=7, minute=0, second=0, microsecond=0)

walking = 'Ходьба не беговой'
walking_start = now + timedelta(days=1)
walking_start = walking_start.replace(hour=10)
walking_end = walking_start.replace(hour=10, minute=45)

regular_event = RegularEvent.get_object(name=walking)
Event.create(regular_event=regular_event.id, start=walking_start, end=walking_end, title={'value': walking})

Message.simple_message(transport=NotificationTransport.telegram(), extra_data={'title': f'{walking} запланировано на завтра с 10:00 до 10:45'})
