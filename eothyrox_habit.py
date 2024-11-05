import os
import sys

from app.habit.models import UserHabitRecord, UserHabit
from app.stockRoom.models import Stock, StockItem, Measure, UserStockRoomItem

sys.path.append('./')

objects = UserHabitRecord.get_objects()
user_habit_record = UserHabitRecord.get_object(os.environ["object_id"])
user_habit = UserHabit.get_object(user_habit_record.user_habit)

stock_item = StockItem.get_objects(name='Eothyrox')[0]
pieces = Measure.get_objects(name='Штук')[0]
pack = Measure.get_objects(name='Упаковка')[0]
stock = Stock.get_objects(name='Private and isolated')[0]

user_stock_room_item = UserStockRoomItem.get_objects(stock_room_item=stock_item.id, measure=pieces.id)
if not user_stock_room_item:
    print('no items')
    user_stock_room_item = UserStockRoomItem.get_objects(stock_room_item=stock_item.id, measure=pack.id)
    print('exists!!')
else:
    print('!!!!!')
    print(user_stock_room_item)
