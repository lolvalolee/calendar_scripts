import sys

from app.calendar.models import RegularEvent

sys.path.append('./')

r = RegularEvent.get_object(1)

print(r._data)
print(r.events())
