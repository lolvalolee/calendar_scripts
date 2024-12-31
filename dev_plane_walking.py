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
        'start': datetime.combine(start.date(), time(*map(int, meal_schedule.start.split(':'))), tz),
        'end': datetime.combine(start.date(), time(*map(int, meal_schedule.end.split(':'))), tz),
        'meal_items': [
            dict(stock=stock.id,  **item) for item in recipe_items
        ]
    }
    Meal.create(**data)
