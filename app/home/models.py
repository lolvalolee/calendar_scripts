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
