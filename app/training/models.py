from dataclasses import dataclass

from utils.models import CRUDModel


@dataclass
class UserExercise(CRUDModel):
    url = '/api/point-type/'

    name: dict
    total_amount: float

