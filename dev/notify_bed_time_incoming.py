from datetime import timedelta, datetime

from app.calendar.models import RegularEvent, Event
from app.handler.constants import ACTION_CALL_HANDLER
from app.home.models import MainPageDisplay
from app.notification.models import Message, NotificationTransport
from app.profile.models import Profile
from app.stockRoom.constants import STATUS_IN_STOCK_ROOM
from app.stockRoom.models import UserStockRoomItem


def handle():
    profile = Profile.get()

    current_events = list(Event.current_events())
    allowed_events = ['Сон', 'Ходьба на беговой', 'Ванна']
    print(current_events)
    if not current_events or list(filter(lambda e: e.title['value'] in allowed_events, current_events)):
        questions = [
            {
                'title': 'Иду в душ',
                'action': {
                    'type': ACTION_CALL_HANDLER,
                    'qs': {'name': 'take_reward'},
                    'handler_extra_data': {'i': '+'}
                }
            },
            {
                'title': 'Чуть позже',
                'action': {
                    'type': ACTION_CALL_HANDLER,
                    'qs': {'name': 'take_reward'},
                    'handler_extra_data': {'i': '+'}
                }
            },
        ]

        extra_data = {
            'title': 'Через час спать. Сейчас - в душ на горшок и в люлю!',
            'questions': questions
        }

        Message.question(transport=NotificationTransport.desktop(), extra_data=extra_data)

    exit(0)
