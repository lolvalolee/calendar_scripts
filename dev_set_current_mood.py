import json
import os
import sys

from app.profile.models import UserStatus


sys.path.append('./')

statuses, _ = UserStatus.get_objects()

data = json.loads(os.environ.get('handler_extra_data'))
