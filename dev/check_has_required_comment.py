from app.habit.models import UserHabitRecord
from app.tag.models import Comment
from app.notification.models import Message, NotificationTransport


def handle():
    objects, _ = UserHabitRecord.get_objects(extra_data__note_required=True)
    for obj in objects:
        if not Comment.exists(extra_data__uuid=obj.extra_data['uuid']):
            for transport in [NotificationTransport.telegram(), NotificationTransport.desktop()]:
                Message.simple_messagev2(
                    f'Ты забил на одно из запланировных дел. Обьясни в чем причина. Создай нотификацию с uuid {obj.extra_data["uuid"]}', transport)
            print('comment not exist', obj.extra_data)
        else:
            print('comment exist', obj.extra_data['uuid'])
