from app.habit.models import UserHabit
# '❌'

habit, _ = UserHabit.get_objects()
print(habit)
for item in habit:
    print(item.results())
