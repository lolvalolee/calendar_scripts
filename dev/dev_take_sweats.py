from datetime import timedelta

from app.calendar.models import RegularEvent
from app.profile.models import Profile
from app.reward.models import PointType


def handle():
    profile = Profile.get()

    point_type = PointType.get_object(name='Сладости')
    print(f'amount: {point_type.total_amount}')
    if point_type.total_amount > 0:
        print('too low!')
        exit(0)

    start = profile.now
    end = start + timedelta(minutes=15)
    regular_event = RegularEvent.get_object(name='Есть вкусняшки')
    regular_event.start(start=start.isoformat(), end=end.isoformat())
