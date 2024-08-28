import sys

from app.calendar.models import RegularEvent

sys.path.append('./')

print(RegularEvent.get_object(1))
