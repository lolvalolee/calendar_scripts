from datetime import timedelta, datetime

from app.calendar.models import RegularEvent
from app.home.models import MainPageDisplay
from app.notification.models import Message, NotificationTransport
from app.profile.models import Profile
from app.stockRoom.constants import STATUS_IN_STOCK_ROOM
from app.stockRoom.models import UserStockRoomItem


def handle():
    profile = Profile.get()
    start = profile.now
    end = start + timedelta(hours=24)
    # items, cnt = UserStockRoomItem.get_objects(exp_date__lte=end, exp_date__gte=start, status=STATUS_IN_STOCK_ROOM)
    # if not cnt:
    #     exit(0)

    items, cnt = UserStockRoomItem.get_objects()
    # if not cnt:
    #     exit(0)

    items = ' '.join([item.stock_room_item['name']['value'] for item in items])
    msg = f'У {items} сегодня заканчивается срок годности. Не забудь!'
    Message.simple_messagev2(transport=NotificationTransport.telegram(), title=msg)

    regular_event = RegularEvent.get_object(name='готовка')
    subtask, created = regular_event.create_subtask(
        title={'value': f'Приготовить {msg}. Ну или выкинуть'}, extra_data={'test': datetime.now().isoformat()})
    if created:
        MainPageDisplay.assign(subtask)
