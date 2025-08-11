from dataclasses import dataclass
from datetime import datetime

from utils.models import CRUDModel


class MainPageDisplay(CRUDModel):
    url = '/api/main-page-display/'

    position: int
    display_from: datetime
    display_to: datetime
    object_id: int
    content_type_id: int
    content_object: dict
    content_object_verbose_name: str
    extra_data: dict

    @classmethod
    def assign(cls, obj, date_from=None, date_to=None, extra_data=None):
        cls.create(object_id=obj.id, content_type_id=obj.content_type_id, date_from=date_from, date_to=date_to,
                   extra_data=extra_data)
