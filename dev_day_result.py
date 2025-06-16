import sys

from datetime import timedelta, datetime
from zoneinfo import ZoneInfo

sys.path.append('./')

from interval import interval

from app.calendar.models import Event
from app.habit.models import UserHabit
from app.tag.models import Comment
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
percent = total /  (60 * 60 * 24) * 100
print(percent)
print(total)

#
# msg += f'{ok_text if total > 50 else failed} {int(percent)}% времени записано'
# result += int((4 * percent) / 100)
#
# habits = [
#     ('Ел сладкое', 1),
#     ('Eothyrox', 1),
#     ('Posture up 40 минут', 1),
#     ('Встал вовремя', 1),
#     ('Лег спать вовремя', 1),
#     ('Задротил', 1),
#     ('Отвлекался от работы на ютуб\твич', 1, True)
# ]
#
# for habit_title, points, *_reverse_result in habits:
#     habit = UserHabit.get_object(name=habit_title)
#     habit_result = habit.completed_at_date(today_date)
#     if habit_result is None:
#         msg += f'\n{undefined} {habit_title}'
#         continue
#
#     if _reverse_result:
#         msg += f'\n{ok_text if not habit_result else failed} {habit_title}'
#         result += points if not habit_result else 0
#     else:
#         msg += f'\n{ok_text if habit_result else failed} {habit_title}'
#         result += points if habit_result else 0
#
#
# comments, _ = Comment.get_objects(tag=['дневник', ], created__day=today_date.isoformat())
#
# msg += f'\nDay result: 11/{result}'
#
# Message.simple_message(transport=NotificationTransport.telegram(), extra_data={'title': msg})
