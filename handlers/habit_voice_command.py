from app.habit.constants import RESULT_COMPLETED, RESULT_FAILED
from app.habit.models import UserHabit
from app.notification.models import Message, NotificationTransport
from handlers.constants import HABIT_RESULT_MAPPING


_habit_mapping = {
    'задротил': ['затратил', ]
}

habit_mapping = {}
[habit_mapping.update({_value: key for _value in value}) for key, value in _habit_mapping.items()]
habit_mapping.update({key: key for key in _habit_mapping.keys()})


def handle_habit_report(match):
    habit_name = match.group('habit_name').lower()
    habit_name = habit_mapping.get(habit_name, habit_name)
    try:
        habit = UserHabit.get_object(name=habit_name)
        try:
            result = HABIT_RESULT_MAPPING[match.group('result').lower()]
        except AttributeError:
            result = RESULT_COMPLETED
        habit.report(result)
    except IndexError:
        Message.simple_message(transport=NotificationTransport.telegram(),
                               extra_data={'title': f'Привычка : {habit_name} не найдена'})
