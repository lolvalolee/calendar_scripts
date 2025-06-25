from app.notification.models import NotificationTransport
from app.social.models import Friend


exit(0)
transport = NotificationTransport.telegram()
friends, _ = Friend.get_objects()

for item in friends:
    print(item.send_simple_message('кусь!', transport))
