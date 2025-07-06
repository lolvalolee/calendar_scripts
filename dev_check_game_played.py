import sys

import requests

from datetime import timedelta

from app.calendar.models import RegularEvent, Event
from app.notification.models import Message, NotificationTransport

sys.path.append('./')

from app.profile.models import Profile, ApiKey

profile = Profile.get()

steam_api_key = ApiKey.get_object(name='steam')
print(steam_api_key)

steam_id = "76561198082140903"  # Замените на ваш SteamID
api_key = steam_api_key.key

url = f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={api_key}&steamids={steam_id}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
    if "response" in data and "players" in data["response"]:
        player = data["response"]["players"][0]

        if "gameextrainfo" in player:
            game = player["gameextrainfo"]
            print(f"Вы играете в игру: {game}")
        else:
            print("Вы сейчас не играете в игру.")
    else:
        print("Информация о пользователе не найдена.")
else:
    print("Ошибка при выполнении запроса.")
