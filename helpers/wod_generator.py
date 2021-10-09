import random
from .wod_types import types
from .wod_exercises import exercises


def wod_generator():
    wod = None

    type_index = random.randint(0, len(types)-1)
    type = types[type_index]
    wod = type
    
    number_exercises = random.randint(3, 6)
    wod["exercises"] = []
    while number_exercises > 0:
        exercise_index = random.randint(0, len(exercises) - 1)
        wod["exercises"].append(exercises[exercise_index])
        number_exercises -= 1

    return wod
