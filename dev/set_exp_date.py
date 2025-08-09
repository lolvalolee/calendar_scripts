import os

from app.notification.models import Message, NotificationTransport
from utils.misc import get_handler_extra_data
from app.stockRoom.models import UserStockRoomItem, StockItem


def handle():
    extra_data = get_handler_extra_data()
    print(extra_data)
    # item = UserStockRoomItem.get_object(os.environ['object_id'])
    # stock_item = StockItem.get_object(item.stock_room_item['id'])
