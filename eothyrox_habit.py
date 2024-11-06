import os
import sys

from app.habit.models import UserHabitRecord, UserHabit
from app.notification.models import Message, NotificationTransport
from app.stockRoom.constants import STATUS_IN_STOCK_ROOM, STATUS_PLANNED
from app.stockRoom.models import Stock, StockItem, Measure, UserStockRoomItem

sys.path.append('./')

objects = UserHabitRecord.get_objects()
user_habit_record = UserHabitRecord.get_object(os.environ["object_id"])
user_habit = UserHabit.get_object(user_habit_record.user_habit)

desktop = NotificationTransport.desktop()
telegram = NotificationTransport.telegram()

stock_item, _ = StockItem.get_objects(name='Eothyrox')
piece, _ = Measure.get_objects(name='Штук')
pack, _ = Measure.get_objects(name='Упаковок')
stock, _ = Stock.get_objects(name='dddd stock user group')

stock_item = stock_item[0]
piece = piece[0]
pack = pack[0]
stock = stock[0]

count = UserStockRoomItem.get_objects_count(
    stock_room_item=stock_item.id, measure=piece.id, status=STATUS_IN_STOCK_ROOM)

packs_count = UserStockRoomItem.get_objects_count(
    stock_room_item=stock_item.id, measure=pack.id, status=STATUS_IN_STOCK_ROOM)
planned_count = UserStockRoomItem.get_objects_count(
    stock_room_item=stock_item.id, measure=pack.id, status=STATUS_PLANNED)

if not count and not packs_count:
    print('no count on stock')
    if not planned_count:
        print('adding to buy')
        [Message.simple_message(
            transport=transport.id, extra_data={'title': 'Eothyrox нет на складе. Добавлено к списку покупок'})
            for transport in [desktop, telegram]]
        stock.plane(stock_item.id, pack.id, 2)
    exit(0)

if not count:
    if packs_count:
        stock.use(stock_item.id, pack.id, 1)
        stock.add(stock_item.id, piece.id, 25)
        stock.use(stock_item.id, piece.id, 1)
        packs_count -= 1
else:
    stock.use(stock_item.id, piece.id, 1)

if count < 10 and packs_count == 0 and not planned_count:
    stock.plane(stock_item.id, pack.id, 2)
    [Message.simple_message(transport=desktop, extra_data={'title': 'Eothyrox добавлен в список покупок'})
         for transport in [desktop, telegram]]
