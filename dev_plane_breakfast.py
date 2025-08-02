from app.stockRoom.models import Recipe, Measure, Stock, MealSchedule

from utils.misc import get_handler_extra_data


print(get_handler_extra_data())
extra_data = get_handler_extra_data()
exit(0)
recipe = Recipe.get_object(id=extra_data['recipe_id'])

meal_stock_item = 'гречневая каша'

gm = Measure.get_object(name='Грамм')
stock = Stock.get_object(name='Дом')
recipe_items = []

for item in recipe.recipe_items:
    _recipe_item = item
    _recipe_item['stock_room_item'] = {'name': item['stock_room_item']['name']}
    recipe_items.append(_recipe_item)

stock.plane_to_cook({'name': {'value': meal_stock_item}}, gm.id, 90, recipe_items)

#
# data = {
#     'meal_schedule': meal_schedule.id,
#     'title': {'value': meal_schedule.title['value']},
#     'start': datetime.combine(walking_start.date(), time(*map(int, meal_schedule.start.split(':'))), tz),
#     'end': datetime.combine(walking_start.date(), time(*map(int, meal_schedule.end.split(':'))), tz),
#     'meal_items': [
#         dict(stock=stock.id, **item) for item in recipe_items
#     ]
# }
# Meal.create(**data)