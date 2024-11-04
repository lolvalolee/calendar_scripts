import os
import sys

from app.habit.models import UserHabitRecord, UserHabit
from app.stockRoom.models import Stock

sys.path.append('./')

objects = UserHabitRecord.get_objects()
user_habit_record = UserHabitRecord.get_object(os.environ["object_id"])
user_habit = UserHabit.get_object(user_habit_record.user_habit)

stock = Stock.get_objects(name='Private and isolated')
stock.use()

print('stock:')
print(stock)