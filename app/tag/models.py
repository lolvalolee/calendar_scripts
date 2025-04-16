from dataclasses import dataclass
from datetime import datetime

from utils.models import BaseModel


@dataclass
class Comment(BaseModel):
    url = '/api/comment/'

    name: str
    created: datetime
    text: dict
    tags: list
    object_id = None
    related_object = None
