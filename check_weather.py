import requests

# from dateutil import parser

import sys
from app.notification.models import NotificationTransport, Message

sys.path.append('./')

r = requests.get('https://api.open-meteo.com/v1/forecast?latitude=49.8383&longitude=24.0232&hourly=temperature_2m,rain,showers,snowfall,snow_depth&forecast_days=1')
data = r.json()

desktop = NotificationTransport.telegram()

r = Message.simple_message(transport=desktop, extra_data={'title': 'Next message wil contain weather info'})
