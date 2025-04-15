import sys
from datetime import timedelta, datetime, time
from zoneinfo import ZoneInfo

from interval import interval

from app.calendar.models import RegularEvent, Event
from app.habit.models import UserHabit
from app.stockRoom.models import MealSchedule, Measure, Stock, Recipe, Meal

sys.path.append('./')

from app.profile.models import Profile

result = 0

# no_sugar_today = UserHabit.get_object(name='Ел сладкое')
# eothyrox = UserHabit.get_object(name='Eothyrox')
# posture_app_complete = UserHabit.get_object(name='Posture up 40 минут')
# woke_up_ontime = UserHabit.get_object(name='Встал вовремя')
# went_sleep_ontime = UserHabit.get_object(name='Лег спать вовремя')
# played_games = UserHabit.get_object(name='Задротил')

profile = Profile.get()
tz = ZoneInfo(profile.timezone)

now = datetime.now(tz)
print(now)
events, _ = Event.today_events()

print('events')
print(events)
intervals = interval()

# for event in events:
#     intervals = intervals | interval[max(start, item.start).timestamp(), min(
#         end or datetime.max, item.end).timestamp()]


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# profile = Profile.get()
# tz = profile.user_timezone
# now = profile.now
# start = now.replace(hour=8, minute=0, second=0, microsecond=0)
#
# routine = 'Личная рутина'
# brushing_teeth = 'Чистить зубы'
#
# routine__regular = RegularEvent.get_object(name=routine)
# Event.create(regular_event=routine__regular.id, start=start, end=start + timedelta(minutes=30),
#              title={'value': routine}, sub_tasks=[{'title': {'value': brushing_teeth}}])
#
# walking = 'Ходьба на беговой'
# walking__regular = RegularEvent.get_object(name=walking)
# Event.create(regular_event=routine__regular.id, start=start + timedelta(minutes=30), end=start + timedelta(hours=1),
#              title={'value': walking})
#
# morning_routine = 'Душ'
# walking__regular = RegularEvent.get_object(name=walking)
# breakfast = 'Завтрак'
#
# Event.create(regular_event=routine__regular.id, start=start, end=start + timedelta(minutes=30),
#              title={'value': routine})
#
# Event.create(regular_event=regular_event.id, start=walking_start, end=walking_end, title={'value': walking})
#
# walking_start = now + timedelta(days=1)
# walking_start = walking_start.replace(hour=10)
# walking_end = walking_start.replace(hour=10, minute=45)
#
# evening_walking_start = walking_start + timedelta(hours=13)
# evening_walking_end = walking_end + timedelta(hours=13)
#
# regular_event = RegularEvent.get_object(name=walking)
#
# morning_routine_regular = RegularEvent.get_object(name=morning_routine)
#
# # walking
# Event.create(regular_event=regular_event.id, start=walking_start, end=walking_end, title={'value': walking})
# # eating
# Event.create(regular_event=regular_event.id, start=walking_start + timedelta(minutes=45),
#              end=walking_end + timedelta(minutes=45), title={'value': morning_routine_regular})
# # bath
# Event.create(regular_event=regular_event.id, start=evening_walking_start, end=evening_walking_end,
#              title={'value': walking})
#
#
#
# meal_stock_item = 'гречневая каша'
#
# meal_schedule = MealSchedule.get_object(title__value='завтрак')
# gm = Measure.get_object(name='Грамм')
# stock = Stock.get_object(name='Дом')
# recipe = Recipe.get_object(name=meal_stock_item)
# recipe_items = []
#
# for item in recipe.recipe_items:
#     _recipe_item = item
#     _recipe_item['stock_room_item'] = {'name': item['stock_room_item']['name']}
#     recipe_items.append(_recipe_item)
#
# stock.plane_to_cook({'name': {'value': meal_stock_item}}, gm.id, 90, recipe_items)
#
# data = {
#     'meal_schedule': meal_schedule.id,
#     'title': {'value': meal_schedule.title['value']},
#     'start': datetime.combine(walking_start.date(), time(*map(int, meal_schedule.start.split(':'))), tz),
#     'end': datetime.combine(walking_start.date(), time(*map(int, meal_schedule.end.split(':'))), tz),
#     'meal_items': [
#         dict(stock=stock.id, **item) for item in recipe_items
#     ]
# }
# Meal.create(**data)
