from dataclasses import dataclass

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
        data = {'stock': self.id}
        send_request('post', self.combine_url(self.url + '/use/'), data=data)

#
#
# @dataclass
# class UserHabit(CRUDModel):
#     url = '/api/user-habit/'
#
#     name: dict
#     name_encrypt: str
#     description: str
#     name_on_skip: str
#     name_on_fail: str
#     name_on_complete: str
#     count_daily: int
#     on_skip: int
#     on_fail: int
#     on_complete: int
#     default_choice: str
#     notification_time: time
#     is_system: bool
#     records: list
#     last_completed_record: dict
#     last_skipped_record: dict
#     last_failed_record: dict
#     created: datetime
#     changed: datetime
#
#     count_today: int = 0
#     count_done: int = 0
#     count_skipped: int = 0
#     count_failed: int = 0
#     count_left: int = 0
