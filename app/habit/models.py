from dataclasses import dataclass

from datetime import datetime, time, date

from app.habit.constants import RESULT_COMPLETED
from utils.models import CRUDModel


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
    records = None
    created: datetime
    changed: datetime

    count_today: int = 0
    count_done: int = 0
    count_skipped: int = 0
    count_failed: int = 0
    count_left: int = 0
    record_date: datetime = 0
    last_completed_record = None
    last_skipped_record = None
    last_failed_record = None

    def results(self, **kwargs):
        return UserHabitRecord.get_objects(url=f'/api/user-habit/{self.id}/records/', **kwargs)

    def completed_at_date(self, record_date: date=None):
        if date is None:
            pass
        data, _ = self.results(record_date__day=record_date.isoformat())

        if not _:
            return None
        return len(data) and all((item.result == RESULT_COMPLETED for item in data))

    def report(self, result, report_date=None):
        UserHabitRecord.create(result=result, user_habit=self, report_date=datetime.now().date)
