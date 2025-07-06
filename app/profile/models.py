from dataclasses import dataclass

from datetime import datetime
from zoneinfo import ZoneInfo

from utils.models import CRUDModel


@dataclass
class Profile(CRUDModel):
    url = '/api/profile/'

    first_name: str
    last_name: str
    language: str
    timezone: str
    telegram_nickname: str
    telegram_status: str
    image: str
    statuses: list

    _instance = None

    @classmethod
    def get(cls):
        if cls._instance is None:
            cls._instance = cls(**cls.retrieve(cls.combine_url(cls.url)))
        return cls._instance

    @property
    def user_timezone(self):
        return ZoneInfo(self.timezone)

    @property
    def now(self):
        return datetime.now(self.user_timezone)


@dataclass
class Param(CRUDModel):
    url = '/api/param/'

    name: dict


@dataclass
class ParamRecord(CRUDModel):
    url = '/api/param-record/'

    record: float
    created: datetime
    comment: str


@dataclass
class ApiKey(CRUDModel):
    url = '/api/key/'

    name: str
    key: str


@dataclass
class UserStatus(CRUDModel):
    url = '/api/user-status/'

    name: dict
    is_used: bool

    def label(self):
        return self.name['value']
