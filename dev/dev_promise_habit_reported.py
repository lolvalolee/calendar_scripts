from datetime import timedelta, datetime
from os import environ

from app.calendar.models import RegularEvent
from app.habit.models import UserHabit
from app.home.models import MainPageDisplay
from app.notification.models import Message, NotificationTransport
from app.profile.models import Profile
from app.stockRoom.constants import STATUS_IN_STOCK_ROOM
from app.stockRoom.models import UserStockRoomItem


def handle():
    print('called!')
    item = UserHabit.get_object(environ['object_id'])
    print(item)