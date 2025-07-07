import os
import sys

from app.notification.models import Message, NotificationTransport
from app.profile.models import UserStatus

sys.path.append('./')

statuses, _ = UserStatus.get_objects()

print(os.environ.get('handler_extra_data'))
