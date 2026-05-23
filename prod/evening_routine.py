from app.profile.models import Profile
from app.notification.models import Message, NotificationTransport


def handle():
    profile = Profile.get()

    Message.simple_messagev2('Спокойной ночи! Надеюсь, зубы ты почистил!',
                             NotificationTransport.telegram())
    exit(0)
