from app.notification.models import Message, NotificationTransport
from app.profile.models import Profile
from app.calendar.models import RegularEvent
from app.tag.models import Comment
from dev_plane_walking import regular_event
from utils.dt import DateUtils


def handle():
    profile = Profile.get()
    now = profile.now

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