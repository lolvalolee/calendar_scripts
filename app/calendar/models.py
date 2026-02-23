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
    canceled: bool

    @property
    def duration(self):
        return self.end - self.start if self.end else (max(datetime.utcnow().astimezone(), self.start) - self.start)

    def end_now(self):
        self._call_action('POST', 'end-now')

    @property
    def duration_seconds(self):
        return self.duration.total_seconds()

    @classmethod
    def today_events(cls, **kwargs):
        return cls.get_objects(range_type='today', **kwargs)

    @classmethod
    def yesterday_events(cls, **kwargs):
        return cls.get_objects(range_type='yesterday', **kwargs)

    @classmethod
    def current_events(cls):
        return cls.get_objects(action_name='current')


@dataclass
class SubTask(CRUDModel):
    url = '/api/subtask/'
    model_name = 'SubTask'

    title: dict
    description: dict
    created: datetime
    created_by: dict
    status: str
    extra_data: dict


@dataclass
class PlannedEvent(CRUDModel):
    url = '/api/event-planned/'

    planned: bool
    plane_type: str
    title: dict
    description: str
    event_planned_timer: list
    sub_tasks: list

    def get_planning(self):
        return self._call_action('GET', 'planning')


@dataclass
class RegularEvent(CRUDModel):
    url = '/api/regular-event/'

    archived: bool
    name: dict
    weekdays: list
    public: bool
    started_at: datetime
    max_duration: int
    duration_required: bool
    created: datetime
    tags: list[dict]

    @apply_default_filters('-start')
    def events(self, start=None, end=None, start_lte=None, end_lte=None, start_gte=None, end_gte=None, **kwargs) -> List[Event]:
        return Event.get_objects(regular_event=self.id, start_gte=start_gte)

    @apply_default_filters('-start')
    def get_events(self, start=None, end=None, start_lte=None, end_lte=None, start_gte=None, end_gte=None, **kwargs):
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
        self._call_action('POST', 'end-now')

    def start_now(self, title=None):
        data = {}
        if title:
            data['title'] = {'value': title}

        self._call_action('POST', 'start-now', data=data)

    def start(self, start, title=None, end=None):
        self._call_action('POST', 'start-now',
                          data={'start': start, 'title': title, end: end})

    def create_subtask(self, title, description=None, **kwargs):
        data = dict(title=title, **kwargs)
        if description:
            data['description'] = description

        response = self._call_action('POST', 'sub-task', data=data)
        if response.status_code != 200:
            return response.json(), False

        return SubTask(**response.json()), True
