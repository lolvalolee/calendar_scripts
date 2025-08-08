import os

from utils.misc import get_handler_extra_data
from app.stockRoom.models import UserStockRoomItem, StockItem


def handle():
    item = UserStockRoomItem.get_object(os.environ['object_id'])
    stock_item = StockItem.get_object(item.stock_room_item['id'])
    for tag in stock_item.tags:
        if tag['name'] == 'есть срок годности':
            print('hey')
