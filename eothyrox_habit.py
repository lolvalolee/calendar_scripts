import os
import sys

from app.habit.models import UserHabitRecord, UserHabit
from app.stockRoom.models import Stock, StockItem, Measure

sys.path.append('./')

objects = UserHabitRecord.get_objects()
user_habit_record = UserHabitRecord.get_object(os.environ["object_id"])
user_habit = UserHabit.get_object(user_habit_record.user_habit)

stock_item = StockItem.get_objects(name='Eothyrox')[0]
measure = Measure.get_objects(name='Штук')[0]
print('items')
print(stock_item, measure)

# stock = Stock.get_objects(name='Private and isolated')[0]
# stock.use()
#
# print('stock:')
# print(stock)