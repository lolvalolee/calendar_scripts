from datetime import timedelta, datetime

from app.calendar.models import RegularEvent, Event
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
    if not current_events:
        Message.simple_messagev2(
            f'Ты забил на одно из запланировных дел. Обьясни в чем причина. Создай нотификацию с uuid {obj.extra_data["uuid"]}',
            NotificationTransport.telegram())

    if list(filter(lambda e: e.title['value'] in allowed_events, current_events)):
        print('!!!')
        exit(0)

    exit(0)
