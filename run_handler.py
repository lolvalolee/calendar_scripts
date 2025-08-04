import sys
from importlib import import_module

arguments = sys.argv


if __name__ == '__main__':
    # FIXME: refactor this
    handler_name = arguments[1].replace('.py', '').replace('/', '.')
    module = import_module(handler_name)
    module.handle()
