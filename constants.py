import os

print('*****')
print(os.environ.get('BASE_URL'))
BASE_URL = os.environ.get('BASE_URL')

DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%s%z'
