import os
from datetime import timedelta

from app.notification.models import Message, NotificationTransport
from app.profile.models import Profile
from utils.misc import get_handler_extra_data
from app.stockRoom.models import UserStockRoomItem, StockItem


def handle():
    extra_data = get_handler_extra_data()
    profile = Profile.get()
    now = profile.now
    item = UserStockRoomItem.get_object(extra_data['i'])
    item.set_exp_date((now + timedelta(days=extra_data['d'])).isoformat())
    # stock_item = StockItem.get_object(item.stock_room_item['id'])
