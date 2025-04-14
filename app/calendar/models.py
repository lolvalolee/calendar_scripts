from dataclasses import dataclass
from datetime import datetime
from typing import List

from utils.models import apply_default_filters, CRUDModel


@dataclass
class Event(CRUDModel):
    url = '/api/event/'

    start: datetime
    end: datetime
    title: dict
    sub_tasks: list
    regular_event: int
    event_type: str

    @property
    def duration(self):
        return self.end - self.start if self.end else (max(datetime.utcnow().astimezone(), self.start) - self.start)

    def end_now(self):
        self._call_action('POST', 'end-now')

    @property
    def duration_seconds(self):
        return self.duration.total_seconds()


@dataclass
class PlannedEvent(CRUDModel):
    url = '/api/event-planned/'

    planned: bool
    plane_type: str
    title: dict
    description: str
    event_planned_timer: list
    sub_tasks: list


@dataclass
class RegularEvent(CRUDModel):
    url = '/api/regular-event/'

    name: dict
    weekdays: list
    public: bool
    started_at: datetime
    max_duration: int
    duration_required: bool

    @apply_default_filters('-start')
    def events(self, start=None, end=None, start_lte=None, end_lte=None, start_gte=None, end_gte=None, **kwargs) -> List[Event]:
        return Event.get_objects(regular_event=self.id, start_gte=start_gte)

    def planned_events(self, start_gte=None, end_gte=None, **kwargs):
        return PlannedEvent.get_objects(regular_event=self.id, start_gte=start_gte)

    def current(self):
        obj, _ = Event.get_objects(url=f'/api/regular-event/{self.id}/current/')
        try:
            return obj[0]
        except IndexError:
            return None

    def end_now(self):
        print(self._call_action('POST', 'end-now'))
