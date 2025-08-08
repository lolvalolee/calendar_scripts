import os

from utils.misc import get_handler_extra_data


def handle():
    print('we')
    print(os.environ.get('OBJECT_ID'))
