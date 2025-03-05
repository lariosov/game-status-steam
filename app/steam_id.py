import requests
import re
from bs4 import BeautifulSoup

"""
DO NOT EDIT MANUALY
Telegram: @lariosov
"""


st_accept = "text/html"
st_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"

# формируем хеш заголовков
headers = {"Accept": st_accept, "User-Agent": st_useragent}


def get_steam_id(url) -> str:
    r = requests.get(url=url,
                     headers=headers)

    # считываем текст HTML-документа
    soup = BeautifulSoup(r.content, "lxml")
    div = soup.find("div", 
                    class_="responsive_page_template_content")
    script = div.find("script", 
                      attrs={"type": "text/javascript"}).text

    pattern = re.compile("\d{17}")
    id = re.findall(pattern, string=script)
    user_id = id[0]

    return user_id


if __name__ == "__main__":
    print(get_steam_id(url="https://steamcommunity.com/id/mrlarios"))
