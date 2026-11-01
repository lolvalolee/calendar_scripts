from calendar_scripts.models import Message, NotificationTransport

desktop = NotificationTransport.desktop()


def handle():
    Message.simple_message("Hey!", desktop)
