from constants import BASE_URL
from utils.http import send_request


class BaseModel:
    url = ''

    @classmethod
    def retrieve(cls, url=None):
        return send_request('get', url or BASE_URL + cls.url).json()

    @classmethod
    def get_all_objects(cls):
        objects = []
        url = cls.url
        while True:
            data = cls.retrieve(url)
            objects.extend(data['results'])
            if data['next']:
                url = data['next']
            else:
                break
        return objects
