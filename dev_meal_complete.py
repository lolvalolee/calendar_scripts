import os
import sys
from datetime import datetime, timedelta, time
from zoneinfo import ZoneInfo

from app.calendar.constants import EVENT_TYPE_MEAL
from app.calendar.models import Event

sys.path.append('./')

from app.notification.models import Message, NotificationTransport
from app.profile.models import Profile
from app.stockRoom.models import Meal, MealItem, MealSchedule, Measure, Stock, Recipe, StockItem

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
tz = ZoneInfo(profile.timezone)
now = datetime.now(tz)
now = now.replace(hour=7, minute=0, second=0, microsecond=0)
start = now + timedelta(days=1)
end = now + timedelta(days=2)

# filter events
# if not event: create meal
events, count = Event.get_objects(start__gte=start.isoformat(), event_type=EVENT_TYPE_MEAL)
if not events:
    meal_schedule = MealSchedule.get_object(title__value='обед')
    gm = Measure.get_object(name='Грамм')
    stock = Stock.get_object(name='Private and isolated')
    recipe = Recipe.get_object(name='хлеб из хлеба')
    recipe_items = []

    for item in recipe.recipe_items:
        _recipe_item = item
        _recipe_item['stock_room_item'] = {'name': item['stock_room_item']['name']}
        recipe_items.append(_recipe_item)

    stock.plane_to_cook({'name': {'value': 'хлеб из хлеба'}}, gm.id, 450, recipe_items)
    data = {
        'meal_schedule': meal_schedule.id,
        'title': {'value': meal_schedule.title['value']},
        'start': datetime.combine(start.date(), time(*meal_schedule.start.split(':')), tz),
        'end': datetime.combine(start.date(), time(*meal_schedule.end.split(':')), tz),
        'meal_items': [
            dict(stock=stock.id, **item) for item in recipe_items
        ]
    }
    Meal.create(**data)



# {
#     "action":"manage","action_type":"meal",
#  "data":{"meal_schedule":4,
#          "title":{"value":"обед"},
#          "start":"2024-12-14T12:00:00.414Z",
#          "end":"2024-12-14T12:20:00.414Z",
#          "meal_items":[{"stock":1,"stock_room_item":{"name":{"keys":[],"value":"хлеб из хлеба"}},
#                         "measure":1,"count":"100","recipe_items":[]}]},
#  "requestCode":"dm16y3wxjt5"
# }