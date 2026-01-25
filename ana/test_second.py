from app.notification.models import Message, NotificationTransport
from app.profile.models import Profile


def handle():
    profile = Profile.get()
    Message.simple_messagev2('test message', NotificationTransport.telegram())
