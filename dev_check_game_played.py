import sys
from datetime import timedelta

from app.calendar.models import RegularEvent, Event
from app.notification.models import Message, NotificationTransport

sys.path.append('./')

from app.profile.models import Profile, ApiKey

profile = Profile.get()

steam_api_key = ApiKey.get_object(name='steam')
print(steam_api_key)
