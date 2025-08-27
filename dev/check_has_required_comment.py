from app.habit.models import UserHabitRecord
from app.tag.models import Comment
from utils.misc import get_handler_extra_data


def handle():
    objects, _ = UserHabitRecord.get_objects(extra_data__note_required=True)
    print(objects)
    rs = Comment.create(data={'text': {'value': 'text here'}, 'tags': ['tag1', 'tag2']})
    print(rs.json())
    print(rs)
