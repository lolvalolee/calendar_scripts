from datetime import timedelta, datetime

from app.calendar.models import RegularEvent, Event
from app.home.models import MainPageDisplay
from app.notification.models import Message, NotificationTransport
from app.profile.models import Profile
from app.stockRoom.constants import STATUS_IN_STOCK_ROOM
from app.stockRoom.models import UserStockRoomItem


def handle():
    profile = Profile.get()
    Message.simple_messagev2(transport=NotificationTransport.telegram(), title='test message')
