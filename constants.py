import os

print('*****')
print(os.environ.get('BASE_URL'))
print(os.environ.get('env.BASE_URL'))
print(os.environ)

BASE_URL = os.environ.get('BASE_URL')

DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%s%z'
