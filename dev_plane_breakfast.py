from app.stockRoom.models import Recipe

from utils.misc import get_handler_extra_data


recipe_name = get_handler_extra_data()

recipes, _ = Recipe.get_objects(tag='завтрак')

for recipe in recipes:
    print(recipe)
