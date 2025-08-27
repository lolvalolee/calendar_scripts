from app.habit.models import UserHabitRecord
from utils.misc import get_handler_extra_data


def handle():
    objects, _ = UserHabitRecord.get_objects(extra_data__note_required=True)
    print(objects)
