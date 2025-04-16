from dataclasses import dataclass
from datetime import datetime

from utils.models import BaseModel


@dataclass
class Comment(BaseModel):
    url = '/api/comment/'

    text: str
    created: datetime
    text: dict
    tags: list
    is_main_page_displayed: bool
    object_id: int = None
    related_object: dict = None
