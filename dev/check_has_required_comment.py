from app.habit.models import UserHabitRecord
from app.tag.models import Comment


def handle():
    objects, _ = UserHabitRecord.get_objects(extra_data__note_required=True)
    for obj in objects:
        print(obj.extra_data)
        # rs = Comment.create(text={'value': 'text here'}, tags=['tag1', 'tag2'], extra_data=obj.extra_data)
        # print(rs.extra_data)