from dataclasses import dataclass, fields

from constants import BASE_URL
from utils.http import send_request


@dataclass
class BaseModel:
    url = ''
    id: int

    @classmethod
    def combine_url(cls, url):
        return BASE_URL + url

    @classmethod
    def retrieve(cls, url, **kwargs):
        return send_request('get', url, kwargs).json()

    @classmethod
    def get_object(cls, pk):
        data = cls.retrieve(cls.combine_url(cls.url) + f'{pk}/')
        _data = {'id': data.get('id')}
        return cls(**data)

    @classmethod
    def get_objects(cls, **kwargs):
        objects = []
        url = cls.combine_url(cls.url)
        while True:
            data = cls.retrieve(url, **kwargs)

            [objects.append(cls(**item)) for item in data['results']]

            if data['next']:
                url = data['next']
            else:
                break
        return objects

    def __post_init__(self):
        print(self)
        for field, field_type in fields(self.__class__):
            print('*****')
            print(field)
            print(field_type)
            # d = getattr(self.__class__, field.name)
            # print(dir(d))
            # # print(field.name, getattr(self.__class__, field.name))
