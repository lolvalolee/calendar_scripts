from app.notification.models import NotificationTransport
from app.social.models import Friend


transport = NotificationTransport.desktop()
friends, _ = Friend.get_objects()

for item in friends:
    print(item.send_simple_message('here is text:)', transport))
