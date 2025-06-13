from dataclasses import dataclass

from utils.models import CRUDModel


@dataclass
class Friend(CRUDModel):
    url = '/api/friend/'

    first_name: str
    last_name: str
    custom_label: str
    image: str
    permissions: list
    user_permissions: list
