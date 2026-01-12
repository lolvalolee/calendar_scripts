from datetime import timedelta, datetime

from app.calendar.models import RegularEvent, Event
from app.home.models import MainPageDisplay
from app.notification.models import Message, NotificationTransport
from app.profile.models import Profile
from app.stockRoom.constants import STATUS_IN_STOCK_ROOM
from app.stockRoom.models import UserStockRoomItem


def handle():
    profile = Profile.get()

    print(Event.current_events())
    allowed_events = ['Сон', 'Ходьба на беговой', 'Ванна']
    if list(filter(lambda e: e.name['value'] in allowed_events, Event.current_events())):
        print('!!!')
        exit(0)

    exit(0)