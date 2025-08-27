from app.habit.models import UserHabitRecord
from app.tag.models import Comment


def handle():
    objects, _ = UserHabitRecord.get_objects(extra_data__note_required=True)
    rs = Comment.create(text={'value': 'text here'}, tags=['tag1', 'tag2'])
    for obj in objects:
        print(obj.extra_data)
        # extra_data = {'note_required': True, 'uuid': str(uuid.uuid4())}
        # rs = Comment.create(text={'value': 'text here'}, tags=['tag1', 'tag2'])
