from dataclasses import dataclass
from datetime import datetime

from utils.models import BaseModel, CRUDModel


@dataclass
class Comment(CRUDModel):
    url = '/api/comment/'

    created: datetime
    text: dict
    tags: list
    is_main_page_displayed: bool
    object_id: int = None
    related_object: dict = None
    extra_data: dict = None
