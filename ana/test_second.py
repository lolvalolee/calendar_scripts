from app.notification.models import Message, NotificationTransport
from app.profile.models import Profile
from utils.misc import get_handler_extra_data


def handle():
    profile = Profile.get()
    Message.simple_messagev2('test message', NotificationTransport.telegram())
    print(get_handler_extra_data())
