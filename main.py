import app.steam_id as sid
import app.steam_parser as spr
import time

"""
DO NOT EDIT MANUALY
Telegram: @lariosov
"""


def main(steam_link) -> str:
    id = sid.get_steam_id(url=steam_link)
    status = spr.start_watching(steam_id=id)

    while status[0] is False:
        time.sleep(60) # каждую минуту проверяем
        return status, main(steam_link=steam_link)
    else:
        return status


if __name__ == "__main__":
    print(main(steam_link='https://steamcommunity.com/id/mrlarios'))
