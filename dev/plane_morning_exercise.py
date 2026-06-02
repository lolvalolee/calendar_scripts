from app.training.models import UserExercise, UserTraining

from utils.misc import get_handler_extra_data


def handle():
    exercises = list(UserExercise.get_objects(extra_data__count=5))
    print(UserTraining.create(user_training_exercises=[
        {'user_exercise': item.id, 'count': 1} for item in exercises
    ]))
