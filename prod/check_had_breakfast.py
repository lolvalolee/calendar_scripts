from datetime import timedelta

from app.profile.models import Profile
from app.calendar.models import RegularEvent


def handle():
    profile = Profile.get()
    now = profile.now
    start_gte = now - timedelta(hours=2)

    regular_event = RegularEvent.get_object(name='завтрак')
    print(list(regular_event.get_events(start_gte=start_gte.isoformat())))
