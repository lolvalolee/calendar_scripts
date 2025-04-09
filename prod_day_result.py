from app.habit.models import UserHabit
# '❌'

habit = UserHabit.get_objects()
for item in habit:
    print(item.results())
