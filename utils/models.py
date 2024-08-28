from constants import BASE_URL
from utils.http import send_request


class BaseModel:
    url = ''
    _data = {}
    id = None

    def __init__(self, data):
        self._data = data
        self.id = data.get('id')

    @classmethod
    def combine_url(cls, url):
        return BASE_URL + url

    @classmethod
    def retrieve(cls, url, **kwargs):
        return send_request('get', url, kwargs).json()

    @classmethod
    def get_object(cls, pk):
        return cls(cls.retrieve(cls.combine_url(cls.url) + f'{pk}/'))

    @classmethod
    def get_objects(cls, **kwargs):
        objects = []
        url = cls.combine_url(cls.url)
        while True:
            data = cls.retrieve(url, **kwargs)
            objects.extend(data['results'])
            if data['next']:
                url = data['next']
            else:
                break
        return objects
