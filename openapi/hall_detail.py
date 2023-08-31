import requests
from bs4 import BeautifulSoup
from decouple import config


def get_hall_detail(hall_id):
    url = f"http://kopis.or.kr/openApi/restful/prfplc/{hall_id}"
    params = {
        "service": config("API_KEY")
    }

    response = requests.get(url, params)
    db = BeautifulSoup(response.content, "lxml")

    seats_count = int(db.seatscale.text.strip())

    if seats_count <= 100:
        seats_count = 100

    return {
        "name": db.fcltynm.text.strip(),
        "address": db.adres.text.strip(),
        "seats_count": seats_count
    }
