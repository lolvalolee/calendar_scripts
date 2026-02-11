from app.handler.constants import ACTION_CALL_HANDLER
from app.notification.models import Message, NotificationTransport
from app.stockRoom.models import Stock, StockItem
from utils.misc import get_handler_extra_data


def handle():
    data = get_handler_extra_data()

    if data:
        stock = Stock.get_object(id=1)
        print(stock)
        stock_room_item = StockItem.get_object(name=data['i'], stock=stock.id)
        print(stock_room_item)
        exit(0)

    meal = ['opti meal', 'purina']
    questions = [
        {
            'title': item,
            'action': {
                'type': ACTION_CALL_HANDLER,
                'qs': {'name': 'test'},
                'handler_extra_data': {'i': item}
            }
        }
        for item in meal
    ]

    extra_data = {
        'title': 'Чем сегодня задабривал зверя?',
        'questions': questions
    }

    Message.question(transport=NotificationTransport.telegram(), extra_data=extra_data)
