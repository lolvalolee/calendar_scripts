from app.habit.models import UserHabitRecord
from app.tag.models import Comment


def handle():
    objects, _ = UserHabitRecord.get_objects(extra_data__note_required=True)
    for obj in objects:
        print(obj.extra_data)
        if not Comment.exists(extra_data__uuid=obj.extra_data['uuid']):
            print('comment not exist', obj.extra_data)
