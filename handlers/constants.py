from app.habit.constants import RESULT_COMPLETED, RESULT_FAILED

_habit_result_mapping = {
    RESULT_COMPLETED: ['выполнен',],
    RESULT_FAILED: ['провал',]
}
HABIT_RESULT_MAPPING = {}
[HABIT_RESULT_MAPPING.update({_value: key for _value in value}) for key, value in _habit_result_mapping.items()]

HABIT_ACTION_REPORT = 'отметь'

VOICE_COMMAND_REGEXPS = [
    f'^(?P<action>{HABIT_ACTION_REPORT}) привычку (?P<habit_name>.+) (?P<result>{"|".join(HABIT_RESULT_MAPPING.keys())})',
    r'^((?P<action>начни|закончи) (?P<regular>регулярное )?событие (?P<event_name>.+))'
]

ACTION_EVENT_START = 'начни'
