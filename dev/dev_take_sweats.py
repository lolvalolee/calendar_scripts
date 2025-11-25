from app.calendar.models import RegularEvent

def handle():
    regular_event = RegularEvent.get_object(name='Есть вкусняшки')
    regular_event.start()
    pass