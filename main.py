import app.steam_id as sid
import app.steam_parser as spr
import time

"""
DO NOT EDIT MANUALY
Telegram: @lariosov
"""


status_counter = 0


def main(steam_link) -> str:
    global status_counter
    id = sid.get_steam_id(url=steam_link)
    status = spr.start_watching(steam_id=id)

    while status[0] is False:
        time.sleep(60) # каждую минуту проверяем
        status_counter = 0
        return status[0], main(steam_link=steam_link)
    else:
        if status_counter == 0:
            status_counter += 1
            return status, main(steam_link=steam_link)
        else:
            time.sleep(60)
            status = True, 'Still in game.'
            return status, main(steam_link=steam_link)


if __name__ == "__main__":
    print(main(steam_link='https://steamcommunity.com/id/mrlarios'))
