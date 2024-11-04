from dataclasses import dataclass
from datetime import datetime
from typing import List

from utils.models import apply_default_filters, CRUDModel


@dataclass
class UserHabitRecord(CRUDModel):
    url = '/api/habit-record/'

    result: str
    record_date: datetime
    user_habit: int
