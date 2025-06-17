from dataclasses import dataclass

from utils.models import CRUDModel


@dataclass
class PointType(CRUDModel):
    url = '/api/point-type/'

    name: dict
    total_amount: float
