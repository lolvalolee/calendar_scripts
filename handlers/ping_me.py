import sys

sys.path.append('../')

from utils.http import send_request

print(send_request('get', 'http://web:8000/api/condition/'))
