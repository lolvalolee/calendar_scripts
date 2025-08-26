from datetime import timedelta, datetime
from os import environ

from app.calendar.models import RegularEvent
from app.habit.constants import RESULT_FAILED
from app.habit.models import UserHabit, UserHabitRecord
from app.home.models import MainPageDisplay
from app.notification.models import Message, NotificationTransport
from app.profile.models import Profile
from app.stockRoom.constants import STATUS_IN_STOCK_ROOM
from app.stockRoom.models import UserStockRoomItem


def handle():
    print('called!')
    item = UserHabitRecord.get_object(environ['object_id'])
    if item.result == RESULT_FAILED:
        item.update(extra_data={'note_required': True})

    print(item)
