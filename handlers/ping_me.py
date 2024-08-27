import sys

sys.path.append('../')

from utils.http import send_request

send_request('get', 'web:8000/api/condition/')
