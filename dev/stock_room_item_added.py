import os

from utils.misc import get_handler_extra_data
from app.stockRoom.models import UserStockRoomItem


def handle():
    item = UserStockRoomItem.get_object(os.environ['object_id'])
    print(item)
