import sys

from app.calendar.models import RegularEvent

sys.path.append('./')

r = RegularEvent.get_object(1)

for i in r.events():
    print(i)
    print(i.start)
