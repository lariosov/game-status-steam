import os
import requests
import json
from dotenv import main


# достаем переменные
main.load_dotenv()

"""
DO NOT EDIT MANUALY
Telegram: @lariosov
"""


def start_watching(steam_id) -> int:

    key = os.getenv("STEAM_API_TOKEN")
    url = f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={key}&steamids={steam_id}"

    dirt_url = requests.get(url=url)
    dirt_text = dirt_url.text
    dirt_row = json.loads(dirt_text)

    for response in dirt_row.keys():

        status = False

        name = dirt_row[response]["players"][0]["personaname"]

        try:
            game = dirt_row[response]["players"][0]["gameextrainfo"]
            status = True
            return status, f"Алярма!\n{name} зашёл в {game}"
        except KeyError:
            return status, f"Скучный {name} сейчас оффлайн."


if __name__ == "__main__":
    print(start_watching(steam_id=76561198130034712))
