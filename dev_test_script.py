from app.calendar.models import PlannedEvent


for e in PlannedEvent.get_objects():
    print(e.get_planning())
