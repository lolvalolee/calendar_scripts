from app.handler.constants import ACTION_CALL_HANDLER
from app.notification.models import Message, NotificationTransport
from app.stockRoom.models import Stock, StockItem, Measure
from utils.misc import get_handler_extra_data


def handle():
    data = get_handler_extra_data()

    if data:
        if data.get('m'):
            Message.simple_messagev2('here!')
            print(data)
            exit(0)

            stock = Stock.get_object(id=1)
            measure = Measure.get_object(name=data['m'])
            stock_room_item = StockItem.get_object(name=data['i'], stock=stock.id)
            print(stock.use(stock_room_item_id=stock_room_item.id, measure_id=measure.id, count=1))
        else:
            questions = [
                {
                    'title': measure.name,
                    'action': {
                        'type': ACTION_CALL_HANDLER,
                        'qs': {'name': 'test'},
                        'handler_extra_data': {'i': data['i'], 'm': measure.id},
                    }
                }
                for measure in Measure.get_objects()
            ]

            extra_data = {
                'title': 'Сколько?',
                'questions': questions
            }

            Message.question(transport=NotificationTransport.telegram(), extra_data=extra_data)

        exit(0)


    stock = Stock.get_object(id=1)

    questions = [
        {
            'title': item.name['value'],
            'action': {
                'type': ACTION_CALL_HANDLER,
                'qs': {'name': 'test'},
                'handler_extra_data': {'i': item.id}
            }
        }
        for item in UserStockRoomItem.get_objects(stock=stock.id)
    ]

    extra_data = {
        'title': 'Предметы склада',
        'questions': questions
    }

    Message.question(transport=NotificationTransport.telegram(), extra_data=extra_data)



    exit(0)


    stock = Stock.get_object(id=1)

    questions = [
        {
            'title': item.name['value'],
            'action': {
                'type': ACTION_CALL_HANDLER,
                'qs': {'name': 'test'},
                'handler_extra_data': {'i': item.id}
            }
        }
        for item in StockItem.get_objects(stock=stock.id)
    ]

    extra_data = {
        'title': 'Предметы склада',
        'questions': questions
    }

    Message.question(transport=NotificationTransport.telegram(), extra_data=extra_data)

    exit(0)



    meal =  ['opti meal', 'purina', 'авфавыаы']
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
