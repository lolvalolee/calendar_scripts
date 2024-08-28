from dataclasses import dataclass
from datetime import datetime

from utils.models import BaseModel


@dataclass
class RegularEvent(BaseModel):
    url = '/api/regular-event/'

    name: dict
    weekdays: list
    public: bool
    delayed_start_at: bool
    started_at: datetime
    max_duration: int
    duration_required: bool

    def events(self, start=None, end=None):
        return Event.get_objects(regular_event=self.id)


@dataclass
class Event(BaseModel):
    url = '/api/event/'

    start: datetime
    end: datetime
    title: dict
    sub_tasks: list
    regular_event: int


