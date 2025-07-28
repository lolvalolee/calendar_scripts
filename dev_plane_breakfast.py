import json
import os


print(json.loads(os.environ.get('handler_extra_data')))