import sys

from app.notification.models import Message, NotificationTransport

sys.path.append('./')

desktop = NotificationTransport.desktop()

r = Message.simple_message(transport=desktop, extra_data={'title': 'You have been notified'})
