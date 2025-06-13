from dataclasses import dataclass

from constants.api_urls import API_URL_FRIEND_MESSAGE

from app.notification.constants import NOTIFICATION_MESSAGE
from utils.misc import send_request
from utils.models import CRUDModel


@dataclass
class Friend(CRUDModel):
    url = '/api/friend/'

    first_name: str
    last_name: str
    custom_label: str
    image: str
    permissions: list
    user_permissions: list

    def send_message(self, text: str, message_type: str, transport):
        return send_request('post', self.combine_url(API_URL_FRIEND_MESSAGE),
                         data={'extra_data': {'title': text},
                               'transport': transport.id,
                               'id': self.id,
                               'notification_type': message_type})

    def send_simple_message(self, text, transport):
        return self.send_message(text, NOTIFICATION_MESSAGE, transport)
