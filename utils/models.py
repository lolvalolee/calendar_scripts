from constants import BASE_URL
from utils.http import send_request


class BaseModel:
    url = ''
    _data = {}

    def __init__(self, data):
        self._data = data
        pass

    @classmethod
    def combine_url(cls, url):
        return BASE_URL + url

    @classmethod
    def retrieve(cls, url, data={}):
        return send_request('get', url, data).json()

    @classmethod
    def get_object(cls, pk):
        return cls(cls.retrieve(cls.combine_url(cls.url) + f'{pk}/'))

    @classmethod
    def get_objects(cls, filters={}):
        objects = []
        url = cls.combine_url(cls.url)
        while True:
            data = cls.retrieve(url, filters)
            objects.extend(data['results'])
            if data['next']:
                url = data['next']
            else:
                break
        return objects
