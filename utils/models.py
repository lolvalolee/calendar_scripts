from constants import BASE_URL
from utils.http import send_request


class BaseModel:
    url = ''

    @classmethod
    def combine_url(cls, url):
        return BASE_URL + url

    @classmethod
    def retrieve(cls, url):
        return send_request('get', url).json()

    @classmethod
    def get_all_objects(cls):
        objects = []
        url = cls.combine_url(cls.url)
        while True:
            data = cls.retrieve(url)
            objects.extend(data['results'])
            if data['next']:
                url = data['next']
            else:
                break
        return objects
