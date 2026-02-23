from app.profile.models import Profile
from app.calendar.models import RegularEvent


def handle():
    profile = Profile.get()
    now = profile.now

    regular_event = RegularEvent.get_object(name='завтрак')
    print(regular_event)
    print(regular_event.events)
