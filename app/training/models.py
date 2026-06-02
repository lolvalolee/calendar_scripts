from dataclasses import dataclass

from utils.models import CRUDModel


@dataclass
class UserExercise(CRUDModel):
    url = '/api/user-exercise/'

    name: dict
    total_amount: float
    extra_data: dict


class UserTrainingExercise(CRUDModel):

    user_training: int
    user_exercise: int
    count : int
    position: int
    count_done: int
    done: bool


class UserTraining(CRUDModel):
    url = '/api/user-training/'
    
    user_training_exercises: list
