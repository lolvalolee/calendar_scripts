import datetime
from dataclasses import dataclass, fields
from json import JSONDecodeError

from constants import BASE_URL
from utils.misc import send_request


def apply_default_filters(*default_filters):
    def decorator(function):
        def wrapper(*args, **kwargs):
            filters = kwargs.pop('filters', default_filters)
            result = function(*args, filters=filters, **kwargs)
            return result
        return wrapper
    return decorator


@dataclass
class BaseModel:
    url = ''
    id: int

    @classmethod
    def combine_url(cls, url):
        return BASE_URL + url

    @classmethod
    def retrieve(cls, url, **kwargs):
        return send_request('get', url, data=kwargs).json()

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
            total_count = data.get('count')
            [objects.append(cls(**item)) for item in data['results']]

            if data['next']:
                url = data['next']
            else:
                break
        return objects, total_count

    @classmethod
    def get_objects_count(cls, **kwargs):
        data, count = cls.get_objects(**kwargs)
        return sum(map(lambda item: float(item.count), data))

    def __post_init__(self):
        for field in fields(self.__class__):
            if field.type == datetime.datetime:
                value = getattr(self, field.name)
                if not value:
                    continue
                setattr(self, field.name, datetime.datetime.strptime(
                    value, '%Y-%m-%dT%H:%M:%S.%f%z').astimezone())

    @classmethod
    def search(cls, search):
        return cls.get_objects(search=search)


class CRUDModel(BaseModel):

    @classmethod
    def create(cls, **kwargs):
        r = None

        for k, v in kwargs.items():
            if isinstance(v, BaseModel):
                kwargs[k] = v.id

        try:
            r = send_request('post', cls.combine_url(cls.url), data=kwargs)
            return r.json()
        except JSONDecodeError:
            print(r)
            print(dir(r))
            print('response not decoded')
        except Exception as e:
            print('error while execute')
            print(e)
