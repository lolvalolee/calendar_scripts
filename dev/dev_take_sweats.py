from datetime import timedelta

from app.calendar.models import RegularEvent
from app.profile.models import Profile
from app.reward.models import PointType, Reward
from app.tag.models import Comment


def handle():
    profile = Profile.get()

    notes = Comment.get_objects(tag=['тренировка','совет'])
    print(notes)
    text = f"""Через 10 минут треша. Не забывай
- {'\n'.join(notes.text['value'])}"""

    print(text)
    exit(0)

    point_type = PointType.get_object(name='Сладости')
    print(f'amount: {point_type.total_amount}')
    if point_type.total_amount > 0:
        print('too low!')
        exit(0)

    start = profile.now
    end = start + timedelta(minutes=15)
    regular_event = RegularEvent.get_object(name='Есть вкусняшки')
    regular_event.start(start=start.isoformat(), end=end.isoformat())

    rewards, _ = Reward.get_objects()
    questions = [
        {
            'title': reward.name['value'],
            'action': {
                'type': 'call_handler',
                'qs': {'name': 'take_reward'},
                'handler_extra_data': {'i': reward.id}
            }
        } for reward in rewards
    ]

    extra_data = {
        'title': f'{stock_item.name["value"]} сьедобный до',
        'questions': questions
    }


    Message.question(transport=NotificationTransport.telegram(), extra_data=extra_data)