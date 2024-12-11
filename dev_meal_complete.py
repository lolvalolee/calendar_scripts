import os
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

sys.path.append('./')

from app.notification.models import Message, NotificationTransport
from app.profile.models import Profile
from app.stockRoom.models import Meal, MealItem

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
print(now.isoformat())
print(now.date())
# events =