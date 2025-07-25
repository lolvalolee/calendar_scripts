from dataclasses import dataclass
from datetime import datetime

from app.notification.constants import NOTIFICATION_MESSAGE, NOTIFICATION_QUESTION
from utils.models import BaseModel, CRUDModel


@dataclass
class NotificationTransport(BaseModel):
    url = '/api/notification-transport/'

    name: str

    @classmethod
    def desktop(cls):
        return cls.search('desktop')[0]

    @classmethod
    def telegram(cls):
        return cls.search('telegram')[0]


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

    @classmethod
    def simple_messagev2(cls, title, transport):
        return cls.create(notification_type=NOTIFICATION_QUESTION, extra_data={'title': title}, transport=transport)

    @classmethod
    def question(cls, **kwargs):
        kwargs['notification_type'] = NOTIFICATION_QUESTION
        return cls.create(**kwargs)
