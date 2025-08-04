import sys
from datetime import datetime, timedelta

from app.calendar.models import Event, RegularEvent
from app.notification.constants import BUTTON_VARIANT_WARNING
from app.notification.models import Message, NotificationTransport
from app.stockRoom.models import Recipe
from utils.misc import get_handler_extra_data


sys.path.append('./')

mood = get_handler_extra_data()['mood']
_now = datetime.now()

if mood == 'Настроение: хорошее':
    RegularEvent.get_object(name='утренний кофе').start(start_dt=_now + timedelta(minutes=10))

    recipes, _ = Recipe.get_objects(tag='завтрак')

    questions = [
        {
            'title': recipe.stock_room_item['name']['value'],
            'style': BUTTON_VARIANT_WARNING,
            'action': {
                'type': 'call_handler',
                'qs': {'name': 'dev_plane_breakfast.py'},
                'handler_extra_data': {
                    'recipe_id': recipe.id
                }
            }
        } for recipe in recipes
    ]

    extra_data = {
        'title': 'Супер. Тогда кофе, небольшая разминка и завтрак. Что будешь кушать?',
        'questions': questions
    }

    Message.question(transport=NotificationTransport.telegram(), extra_data=extra_data)

    exercises = ['нет', 'беговая', 'растягивания', 'оба']
    questions = [
        {
            'title': exercise,
            'style': BUTTON_VARIANT_WARNING,
            'action': {
                'type': 'call_handler',
                'qs': {'id': 16},
                'handler_extra_data': {
                    'e': exercise
                }
            }
        } for exercise in exercises
    ]

    extra_data = {
        'title': 'Как насчет маленькой тренировки?',
        'questions': questions
    }

    Message.question(transport=NotificationTransport.telegram(), extra_data=extra_data)
