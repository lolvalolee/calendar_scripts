from app.notification.models import Message, NotificationTransport
from app.tag.models import Comment


def handle():
    notes, _ = Comment.get_objects(tag=['тренировка','совет'])
    text = 'Через 10 минут треша. Не забывай: \n' + '\n'.join([f'- {note.text["value"]}' for note in notes])

    Message.simple_messagev2(transport=NotificationTransport.telegram(), title=text)
