from dataclasses import dataclass
from datetime import datetime, date, time
from typing import List

from utils.models import apply_default_filters, CRUDModel


@dataclass
class UserHabitRecord(CRUDModel):
    url = '/api/user-habit-record/'

    result: str
    record_date: datetime
    user_habit: int


@dataclass
class UserHabit(CRUDModel):
    url = '/api/user-habit/'

    name: dict
    name_encrypt: str
    description: str
    name_on_skip: str
    name_on_fail: str
    name_on_complete: str
    count_daily: int
    on_skip: int
    on_fail: int
    on_complete: int
    default_choice: str
    notification_time: time
    is_system: bool
    records: list
    last_completed_record: dict
    last_skipped_record: dict
    last_failed_record: dict
    created: datetime
    changed: datetime

    count_today: int = 0
    count_done: int = 0
    count_skipped: int = 0
    count_failed: int = 0
    count_left: int = 0
