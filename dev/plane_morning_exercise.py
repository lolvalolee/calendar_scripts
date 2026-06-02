from app.training.models import UserExercise

from utils.misc import get_handler_extra_data


def handle():
    exercises = UserExercise.get_objects()
    print(exercises)
    print(get_handler_extra_data())
