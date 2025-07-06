import sys

import requests

sys.path.append('./')

from app.calendar.models import RegularEvent
from app.profile.models import Profile, ApiKey

profile = Profile.get()

steam_api_key = ApiKey.get_object(name='steam')


steam_id = "76561198082140903"  # Замените на ваш SteamID
api_key = steam_api_key.key

url = f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={api_key}&steamids={steam_id}"

response = requests.get(url)
game = None

if response.status_code == 200:
    data = response.json()
    if "response" in data and "players" in data["response"]:
        player = data["response"]["players"][0]

        if "gameextrainfo" in player:
            game = player["gameextrainfo"]
        else:
            exit(0)
else:
    print(f'Unexpected response code: {response.status_code}')
    exit(0)

regular_event = RegularEvent.get_object(name='Задротство')
current = regular_event.current()

if not current and game:
    regular_event.start_now(title=game)
elif current and not game:
    regular_event.end_now()
