from dataclasses import dataclass

from utils.models import CRUDModel


@dataclass
class PointType(CRUDModel):
    url = '/api/point-type/'

    name: dict
    total_amount: float


@dataclass
class PointRecord(CRUDModel):
    url = '/api/point-record/'

    point_type: int
    record: float


@dataclass
class Reward(CRUDModel):
    url = '/api/reward/'

    count: int
    claim_count: int
