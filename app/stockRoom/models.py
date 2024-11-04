from dataclasses import dataclass
from typing import Optional

from utils.misc import send_request
from utils.models import CRUDModel


@dataclass
class Stock(CRUDModel):
    url = '/api/stock/'

    name: str
    user_group: dict
    isolate_stock_items: bool
    default_encryption_keys: list

    def use(self):
        data = {}
        r = send_request('post', self.combine_url(self.url + f'{self.id}/use/'), data=data)
        print('use item')
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
