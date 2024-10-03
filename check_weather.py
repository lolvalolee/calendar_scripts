import requests

import sys
from typing import List

from app.calendar.models import RegularEvent, Event
from app.profile.models import Profile

sys.path.append('./')

r = requests.get('https://api.open-meteo.com/v1/forecast?latitude=49.8383&longitude=24.0232&hourly=temperature_2m,rain,showers,snowfall,snow_depth&forecast_days=1')
print('trying to fetch data')
print(r.json())