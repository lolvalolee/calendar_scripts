import os

API_URL_BASE = '/api/'

API_URL_MESSAGE = f'{API_URL_BASE}messages/friend/'
API_URL_FRIEND_MESSAGE = f'{API_URL_MESSAGE}friend/'

BASE_URL = os.environ.get('base_url')

DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%s%z'
