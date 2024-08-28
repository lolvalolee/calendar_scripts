from utils.http import send_request


class BaseModel:
    url = ''

    @classmethod
    def retrieve(cls, url=None):
        return send_request(url or self.url, 'get').json()

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
