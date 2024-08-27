import os

import requests


def send_request(method, url, data=None, headers=None):
    data = data or {}
    headers = headers or {}

    headers['Authorization'] = f'Bearer {os.environ["TOKEN"]}'
    return getattr(requests, method)(url, data=data, headers=headers)
