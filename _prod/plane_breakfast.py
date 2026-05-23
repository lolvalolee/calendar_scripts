from app.stockRoom.models import Recipe, Measure, Stock, MealSchedule

from utils.misc import get_handler_extra_data


def handle():
    extra_data = get_handler_extra_data()
    recipe = Recipe.get_object(id=extra_data['recipe_id'])

    gm = Measure.get_object(name='Грамм')
    stock = Stock.get_object(name='Дом')
    recipe_items = []

    for item in recipe.recipe_items:
        _recipe_item = item
        _recipe_item['stock_room_item'] = {'name': item['stock_room_item']['name']}
        recipe_items.append(_recipe_item)

    stock.plane_to_cook({'name': {'value': meal_stock_item}}, gm.id, 90, recipe_items)
