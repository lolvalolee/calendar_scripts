import os
import sys

from app.notification.models import Message, NotificationTransport
from app.stockRoom.models import Meal, MealItem

sys.path.append('./')

desktop = NotificationTransport.desktop()
meal = Meal.get_object(os.environ["object_id"])

msg = ''

for item in meal.meal_items:
    meal_item = MealItem.get_object(item['id'])
    msg += f'{meal_item.debt} {meal_item.measure["short_name"]} {meal_item.stock_room_item["name"]["value"]}'
print('sending message!')
Message.simple_message(transport=desktop, extra_data={'title': f'Message :{msg}'})
