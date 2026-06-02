from dataclasses import dataclass

from utils.models import CRUDModel


@dataclass
class UserExercise(CRUDModel):
    url = '/api/point-type/'

    name: dict
    total_amount: float


class UserTrainingExercise(CRUDModel):

    user_training: int
    user_exercise: int
    count : int
    position: int
    count_done: int
    done: bool


class UserTraining(CRUDModel):
    user_training_exercises: list
