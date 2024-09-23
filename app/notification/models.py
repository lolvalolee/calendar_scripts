from dataclasses import dataclass
from datetime import datetime

from app.notification.constants import NOTIFICATION_MESSAGE
from utils.models import BaseModel, CRUDModel


class NotificationTransport(BaseModel):
    url = '/api/notification-transport/'

    name: str

    @classmethod
    def desktop(cls):
        return cls.search('desktop')[0]


@dataclass
class Message(CRUDModel):
    url = '/api/message/'

    notification_type: str
    due_to: datetime
    content_type: int
    object_id: int
    extra_data: dict
    transport: int

    @classmethod
    def simple_message(cls, **kwargs):
        kwargs['notification_type'] = NOTIFICATION_MESSAGE
        return cls.create(**kwargs)
