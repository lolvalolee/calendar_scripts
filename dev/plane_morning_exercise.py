from app.training.models import UserExercise, UserTraining

from utils.misc import get_handler_extra_data


def handle():
    exercises = list(UserExercise.get_objects())
    print(UserTraining.create())
