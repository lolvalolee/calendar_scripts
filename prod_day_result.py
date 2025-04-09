from app.habit.models import UserHabit
# '❌'

habit, _ = UserHabit.get_objects()
for item in habit:
    print(item.results())
