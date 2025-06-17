import sys

from datetime import timedelta, datetime
from zoneinfo import ZoneInfo

from app.reward.models import PointType, PointRecord

sys.path.append('./')

from interval import interval

from app.calendar.models import Event
from app.notification.models import Message, NotificationTransport
from app.profile.models import Profile

result = 0

msg = ''
ok_text = '✅'
failed = '❌'
undefined = '❓'

profile = Profile.get()
tz = ZoneInfo(profile.timezone)

today = datetime.now(tz).replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=1)
today_date = today.date()

tomorrow = today + timedelta(days=1)

events, _ = Event.today_events()

intervals = interval()

for event in events:
    intervals = intervals | interval[max(today, event.start).timestamp(), min(
        tomorrow, event.end or datetime.max.astimezone(tz)).timestamp()]

total = sum(map(lambda _item: _item[1] - _item[0], intervals))
percent = int(((60 * 60 * 24) - total) / 60)

Message.simple_message(transport=NotificationTransport.desktop(),
                       extra_data={'title': f'Снято {percent} баллов за незаписаное время.'})

point_type = PointType.get_object(name='в')

PointRecord.create(point_type=point_type.id, record=-percent)
