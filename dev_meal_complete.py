import os
import sys

from app.stockRoom.models import Stock, StockItem, Measure, UserStockRoomItem, Meal, MealItem

sys.path.append('./')
print('called')

meal = Meal.get_object(os.environ["object_id"])
for item in meal.meal_items:
    print(item)
    # print(MealItem.get_object(item['id']))
