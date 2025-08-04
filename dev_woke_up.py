from app.notification.constants import BUTTON_VARIANT_WARNING
from app.notification.models import Message, NotificationTransport
from app.profile.models import UserStatus


def handle():
    statuses, _ = UserStatus.get_objects()

    questions = [
        {
            'title': item.name['value'],
            'style': BUTTON_VARIANT_WARNING,
            'action': {
                'type': 'call_handler',
                'qs': {'name': 'dev_set_current_mood.py'},
                'handler_extra_data': {
                    'mood': item.label
                }
            }
        } for item in statuses
    ]

    extra_data = {
        'title': 'Сань, какое настроение?',
        'questions': questions
    }

    Message.question(transport=NotificationTransport.telegram(), extra_data=extra_data)








#
# profile = Profile.get()
# tz = profile.user_timezone
# now = profile.now
# now = now.replace(hour=7, minute=0, second=0, microsecond=0)
#
# event_name = 'Event name'
# subtask_name = 'Event subtask name'
#
# Event.create(start=now, end=now + timedelta(hours=2), title={'value': event_name}, sub_tasks=[
#     {'title': {'value': subtask_name}},
# ])
#
# exit(0)
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
# Event.create(regular_event=regular_event.id, start=walking_start, end=walking_end, title={'value': walking})
#
# Event.create(regular_event=regular_event.id, start=walking_start + timedelta(minutes=45),
#              end=walking_end + timedelta(minutes=45), title={'value': morning_routine_regular})
#
# Event.create(regular_event=regular_event.id, start=evening_walking_start, end=evening_walking_end,
#              title={'value': walking})
#
# Message.simple_message(transport=NotificationTransport.desktop(),
#                        extra_data={'title': f'{walking} запланировано на завтра с 10:00 до 10:45'})
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
