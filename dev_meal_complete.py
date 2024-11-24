import os
import sys

from app.habit.models import UserHabitRecord, UserHabit
from app.notification.models import Message, NotificationTransport
from app.stockRoom.constants import STATUS_IN_STOCK_ROOM, STATUS_PLANNED
from app.stockRoom.models import Stock, StockItem, Measure, UserStockRoomItem, Meal

sys.path.append('./')
print('called')

print(Meal.get_object(os.environ["object_id"]))
