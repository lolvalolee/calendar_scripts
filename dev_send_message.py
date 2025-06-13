from app.notification.models import NotificationTransport
from app.social.models import Friend


transport = NotificationTransport.desktop()

for item in Friend.get_objects():
    item.send_simple_message('here is text', transport)
