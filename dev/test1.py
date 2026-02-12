from app.notification.models import NotificationTransport
from app.social.models import Friend


def handle():
    transport = NotificationTransport.telegram()
    friend = Friend.get_object(pk=7)
    friend.send_simple_message('ку-ку!', transport)
