from dataclasses import dataclass
from datetime import datetime

from utils.models import BaseModel


@dataclass
class Message(BaseModel):
    url = '/api/regular-event/'

    name: dict
    weekdays: list
    public: bool
    delayed_start_at: bool
    started_at: datetime
    max_duration: int
    duration_required: bool
    #
    # @apply_default_filters('-start')
    # def events(self, start=None, end=None, start_lte=None, end_lte=None, start_gte=None, end_gte=None, **kwargs) -> List[Event]:
    #     return Event.get_objects(regular_event=self.id, start_gte=start_gte)
    #
    # def planned_events(self, start_gte=None, end_gte=None, **kwargs):
    #     return PlannedEvent.get_ob