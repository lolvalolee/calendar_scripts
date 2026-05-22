from app.profile.models import Profile
from app.notification.models import Message, NotificationTransport


def handle():
    profile = Profile.get()

    Message.simple_messagev2(title='Почисти зубы!')
    exit(0)
