from dataclasses import dataclass
from typing import Optional

from app.calendar.models import Event
from utils.misc import send_request
from utils.models import CRUDModel


@dataclass
class Stock(CRUDModel):
    url = '/api/stock/'

    name: str
    user_group: dict
    isolate_stock_items: bool
    default_encryption_keys: list

    def use(self, stock_room_item_id, measure_id, count):
        data = {'stock_room_item': stock_room_item_id,
                'measure': measure_id,
                'count': count}
        return send_request('post', self.combine_url(self.url + f'{self.id}/use/'), data=data)

    def add(self, stock_room_item_id, measure_id, count):
        data = {'stock_room_item': stock_room_item_id,
                'measure': measure_id,
                'count': count}
        return send_request('post', self.combine_url(self.url + f'{self.id}/add/'), data=data)

    def plane(self, stock_room_item_id, measure_id, count):
        data = {'stock_room_item': stock_room_item_id,
                'measure': measure_id,
                'count': count}
        r =  send_request('post', self.combine_url(self.url + f'{self.id}/plane/'), data=data)
        print(r.json())



@dataclass
class StockItem(CRUDModel):
    url = '/api/stock-room/'
    name: dict


@dataclass
class Measure(CRUDModel):
    url = '/api/measure/'

    name: str
    short_name: str


@dataclass
class UserStockRoomItem(CRUDModel):
    url = '/api/user-stock-room/'

    status: str
    measure: dict
    stock: dict
    reserved_for: Optional[dict]
    count: float
    stock_room_item: dict
    deleted: bool


@dataclass
class MealItems(CRUDModel):
    stock_room_item: StockItem
    stock: Stock
    count: float
    measure: Measure


@dataclass
class Meal(CRUDModel):
    url = '/api/meal/'

    event: Event
    completed: bool

