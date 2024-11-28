import os
import sys

from app.notification.models import Message, NotificationTransport
from app.stockRoom.models import Meal, MealItem

sys.path.append('./')

desktop = NotificationTransport.desktop()
meal = Meal.get_object(os.environ["object_id"])

debt_items = ' '.join([f'{item["debt"]} {item["measure"]["short_name"]} {item["stock_room_item"]["name"]["value"]}' for item in meal.meal_items if item['debt']])
print('sending message!')
Message.simple_message(transport=desktop, extra_data={'title': f'Message :{debt_items}'})