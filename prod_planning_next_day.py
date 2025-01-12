import sys
from datetime import timedelta, datetime, time

from app.calendar.models import RegularEvent, Event
from app.notification.models import Message, NotificationTransport
from app.stockRoom.models import MealSchedule, Measure, Stock, Recipe, Meal

sys.path.append('./')

from app.profile.models import Profile


profile = Profile.get()
tz = profile.user_timezone
now = profile.now
now = now.replace(hour=7, minute=0, second=0, microsecond=0)

walking = 'Ходьба на беговой'
walking_start = now + timedelta(days=1)
walking_start = walking_start.replace(hour=10)
walking_end = walking_start.replace(hour=10, minute=45)

regular_event = RegularEvent.get_object(name=walking)

Event.create(regular_event=regular_event.id, start=walking_start, end=walking_end, title={'value': walking})

Message.simple_message(transport=NotificationTransport.desktop(), extra_data={'title': f'{walking} запланировано на завтра с 10:00 до 10:45'})

meal_stock_item = 'гречневая каша'

meal_schedule = MealSchedule.get_object(title__value='завтрак')
gm = Measure.get_object(name='Грамм')
stock = Stock.get_object(name='Дом')
recipe = Recipe.get_object(name=meal_stock_item)
recipe_items = []

for item in recipe.recipe_items:
    _recipe_item = item
    _recipe_item['stock_room_item'] = {'name': item['stock_room_item']['name']}
    recipe_items.append(_recipe_item)

stock.plane_to_cook({'name': {'value': meal_stock_item}}, gm.id, 90, recipe_items)

data = {
    'meal_schedule': meal_schedule.id,
    'title': {'value': meal_schedule.title['value']},
    'start': datetime.combine(walking_start.date(), time(*map(int, meal_schedule.start.split(':'))), tz),
    'end': datetime.combine(walking_start.date(), time(*map(int, meal_schedule.end.split(':'))), tz),
    'meal_items': [
        dict(stock=stock.id, **item) for item in recipe_items
    ]
}
Meal.create(**data)
