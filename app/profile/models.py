from utils.http import send_request
from utils.models import BaseModel


class Profile(BaseModel):
    url = '/api/profile/'
