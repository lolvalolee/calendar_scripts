from dataclasses import dataclass
from datetime import datetime

from app.notification.constants import NOTIFICATION_MESSAGE
from utils.models import BaseModel


@dataclass
class Message(BaseModel):
    url = '/api/message/'

    name: dict
    weekdays: list
    public: bool
    delayed_start_at: bool
    started_at: datetime
    max_duration: int
    duration_required: bool

    @classmethod
    def simple_message(cls, **kwargs):
        kwargs['notification_type'] = NOTIFICATION_MESSAGE
        return cls.create(**kwargs)
