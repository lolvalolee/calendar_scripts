from datetime import datetime

from app.calendar.models import RegularEvent, Event
from app.notification.models import NotificationTransport, Message

_event_name_mapping = {
    'задротил': ['затратил', ]
}

event_name_mapping = {}
[event_name_mapping.update({_value: key for _value in value}) for key, value in _event_name_mapping.items()]
event_name_mapping.update({key: key for key in _event_name_mapping.keys()})



def start_event(match):
    event_name = match.group('event_name').lower()
    event_name = event_name_mapping.get(event_name, event_name)

    try:
        print(match.group('regular'))
        print('!!!!!!!!!!')
        print('!!!!!!!!!!')
        print('!!!!!!!!!!')
        regular_event = RegularEvent.get_object(name=event_name)
        regular_event.start_now()
    except IndexError:
        Message.simple_message(transport=NotificationTransport.telegram(),
                               extra_data={'title': f'Не найдено регулярного события: {event_name}'})
        return
    except AttributeError:
        Event.get_object(title=event_name, start=datetime.now())

    print(':)')
    print(event_name)

def end_event(match):
    pass
