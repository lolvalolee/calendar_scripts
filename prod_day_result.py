from datetime import datetime

from app.habit.models import UserHabit

now = datetime.now()
# '❌'

habit, _ = UserHabit.get_objects()
for item in habit:
    results, _ = item.results()
    print(results)
