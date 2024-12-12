import os
import sys
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from app.calendar.constants import EVENT_TYPE_MEAL
from app.calendar.models import Event

sys.path.append('./')

from app.notification.models import Message, NotificationTransport
from app.profile.models import Profile
from app.stockRoom.models import Meal, MealItem, MealSchedule

#
# desktop = NotificationTransport.desktop()
# meal = Meal.get_object(os.environ["object_id"])
#
# msg = ''
#
# for item in meal.meal_items:
#     meal_item = MealItem.get_object(item['id'])
#     msg += f'{meal_item.debt} {meal_item.measure["short_name"]} {meal_item.stock_room_item["name"]["value"]}'
#
# Message.simple_message(transport=desktop, extra_data={'title': f'Message :{msg}'})

profile = Profile.get()
ZoneInfo(profile.timezone)
print(ZoneInfo(profile.timezone))
now = datetime.now(ZoneInfo(profile.timezone))
now = now.replace(hour=7, minute=0, second=0, microsecond=0)
start = now + timedelta(days=1)
end = now + timedelta(days=2)


print(now.isoformat())
print(now.date())

# filter events
# if not event: create meal
events, count = Event.get_objects(start__gte=start.isoformat(), event_type=EVENT_TYPE_MEAL)
if  not events:
    meal_schedule, count = MealSchedule.get_objects(title__value='обед')
    meal_schedule = meal_schedule[0]

print(events)