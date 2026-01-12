import datetime

from dataclasses import dataclass, fields
from json import JSONDecodeError
from zoneinfo import ZoneInfo

import dateutil.parser

from constants.api_urls import BASE_URL
from utils.misc import send_request


def apply_default_filters(*default_filters):
    def decorator(function):
        def wrapper(*args, **kwargs):
            filters = kwargs.pop('filters', default_filters)
            result = function(*args, filters=filters, **kwargs)
            return result
        return wrapper
    return decorator


class ObjectsResponse:
    _objects = []
    _count = 0

    def __init__(self, objects, count):
        self._objects = objects
        self._count = count

    def __iter__(self):
        self._index = 0
        return self._objects

    def __next__(self):
        if self._index < len(self.data):
            result = self.data[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

    def __getitem__(self, idx):
        return self._objects[idx]

    def __len__(self):
        return self._count

    def __next__(self):
        if self._index < len(self._count):
            result = self._objects[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration


@dataclass
class BaseModel:
    url = ''
    id: int

    @classmethod
    def combine_url(cls, url):
        return BASE_URL + url

    @classmethod
    def get_api_url(self):
        return self.combine_url(self.url)

    @classmethod
    def retrieve(cls, url, **kwargs):
        return send_request('get', url, data=kwargs).json()

    @classmethod
    def create(cls, url=None, **kwargs):
        return send_request('post', url or cls.get_api_url(), data=kwargs).json()

    @classmethod
    def get_object(cls, pk=None, **kwargs):
        if not pk and kwargs:
            obj, _ = cls.get_objects(**kwargs)
            return obj[0]

        data = cls.retrieve(cls.combine_url(cls.url) + f'{pk}/')
        _data = {'id': data.get('id')}
        return cls(**data)

    @classmethod
    def get_objects(cls, url=None, action_name=None, **kwargs):
        objects = []
        url = cls.combine_url(url or cls.url)

        if action_name:
            url = f'{url}/{action_name}/'

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
                setattr(self, field.name, dateutil.parser.isoparse(value).astimezone(ZoneInfo('UTC')))

    def _call_action(self, method_name='GET', action_name=None, url=None, data=None, **kwargs):
        data = data or {}
        data.update(kwargs)
        return send_request(method_name.lower(), self.combine_url(self.url) + f'{self.id}/{action_name + "/" if action_name else ""}',
                            data=data)

    @classmethod
    def search(cls, search):
        data , _ = cls.get_objects(search=search)
        return data


class CRUDModel(BaseModel):
    model_name = ''

    def _label(self):
        return f'{self.__class__.__name__} {self.id}'

    @property
    def label(self):
        return self._label()

    @classmethod
    def create(cls, **kwargs):
        r = None

        for k, v in kwargs.items():
            if isinstance(v, BaseModel):
                kwargs[k] = v.id

            if isinstance(v, datetime.datetime):
                kwargs[k] = v.isoformat()

        try:
            r = send_request('post', cls.combine_url(cls.url), data=kwargs)
            print(cls.combine_url(cls.url))
            print(r.json())
            return r.json()
        except JSONDecodeError:
            print(r)
            print(dir(r))
            print('response not decoded')
        except Exception as e:
            print('error while execute')
            print(e)

    @property
    def content_type_id(self):
        content_types = get_content_types()
        try:
            return list(filter(lambda x: x['name'] == self.model_name, content_types))[0]['id']
        except IndexError:
            return None

    def update(self, **kwargs):
        return self._call_action('PATCH', data=kwargs)

    @classmethod
    def exists(cls, **kwargs):
        #TODO: rewrite method. it should not retreive all data
        _, cnt = cls.get_objects(**kwargs)
        return bool(cnt)


def get_content_types():
    return send_request('get', f'{BASE_URL}/api/content-type/').json()
