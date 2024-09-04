from dataclasses import dataclass
from zoneinfo import ZoneInfo

from utils.misc import send_request
from utils.models import BaseModel


@dataclass
class Profile(BaseModel):
    url = '/api/profile/'

    first_name: str
    last_name: str
    language: str
    timezone: str
    telegram_nickname: str
    telegram_status: str

    _instance = None

    @classmethod
    def get(cls):
        if cls._instance is None:
            cls._instance = cls(**cls.retrieve(cls.combine_url(cls.url)))
        return cls._instance

    @property
    def user_timezone(self):
        return ZoneInfo(self.timezone)
