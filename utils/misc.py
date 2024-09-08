import json
from datetime import datetime
import os

import requests


def send_request(method, url, data=None, headers=None):
    query_params = {
        'data': data or {},
        'headers': headers or {},
    }

    query_params['headers']['Authorization'] = f'Bearer {os.environ["jwt_token"]}'

    for k, v in query_params['data'].items():
        if not isinstance(v, datetime):
            continue
        query_params['data'][k] = v.isoformat()

    if method == 'get':
        query_params['params'] = query_params['data']

    if method == 'post':
        query_params['data'] = json.dumps(query_params.pop('data', {}))
        query_params['headers']['Content-Type'] = 'application/json'

    return getattr(requests, method)(url, **query_params)
