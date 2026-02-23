from datetime import timedelta

from app.notification.models import Message, NotificationTransport
from app.profile.models import Profile
from app.calendar.models import RegularEvent


def handle():
    profile = Profile.get()
    now = profile.now
    start_gte = now - timedelta(hours=2)

    regular_event = RegularEvent.get_object(name='завтрак')

    if not list(regular_event.get_events(start_gte=start_gte.isoformat())):
        Message.simple_messagev2('Позавтракай!', NotificationTransport.telegram())
    else:
        Message.simple_messagev2('Позавтракал, умничка!', NotificationTransport.telegram())