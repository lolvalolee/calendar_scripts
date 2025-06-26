from app.calendar.models import PlannedEvent

planned, _ = PlannedEvent.get_objects()
for e in planned:
    print(e.get_planning().json())
