import os

from app.notification.models import Message, NotificationTransport
from utils.misc import get_handler_extra_data
from app.stockRoom.models import UserStockRoomItem, StockItem


def handle():
    item = UserStockRoomItem.get_object(os.environ['object_id'])
    stock_item = StockItem.get_object(item.stock_room_item['id'])
    for tag in stock_item.tags:
        if tag['name'] == 'есть срок годности':
            days = range(1, 6)

            questions = [
                {
                    'title': day,
                    'action': {
                        'type': 'call_handler',
                        'qs': {'name': 'set_exp_date'},
                        'handler_extra_data': {
                            'd': day, 'i': item.id,
                        }
                    }
                } for day in days
            ]

            extra_data = {
                'title': f'{stock_item.name["value"]} сьедобный до',
                'questions': questions
            }

            Message.question(transport=NotificationTransport.telegram(), extra_data=extra_data)
