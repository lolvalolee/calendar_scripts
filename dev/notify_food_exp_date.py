from datetime import timedelta

from app.calendar.models import RegularEvent
from app.notification.models import Message, NotificationTransport
from app.profile.models import Profile
from app.stockRoom.constants import STATUS_IN_STOCK_ROOM
from app.stockRoom.models import UserStockRoomItem
from utils.models import get_content_types


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
    subtask, created = regular_event.create_subtask(title={'value': f'Приготовить {msg}. Ну или выкинуть'})
    if created:
        print('create subtask')
        print('created', subtask, subtask.content_type_id)
    else:
        print('not created')
        print(subtask)
    print('***********')
    # print(get_content_types())