from datetime import timedelta

from app.profile.models import Profile
from app.stockRoom.constants import STATUS_IN_STOCK_ROOM
from app.stockRoom.models import UserStockRoomItem


def handle():
    profile = Profile.get()
    start = profile.now
    end = start + timedelta(hours=24)
    items, cnt = UserStockRoomItem.get_objects(exp_date__lte=end, exp_date__gte=start, status=STATUS_IN_STOCK_ROOM)
    items = ' '.join([item.stock_room_item.name['value'] for item in items])
    msg = f'У {items} сегодня заканчивается срок годности. Не забудь!'
    print(items)
