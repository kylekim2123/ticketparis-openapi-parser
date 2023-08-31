import requests
from bs4 import BeautifulSoup


def get_hall_detail(hall_id):
    url = f"http://kopis.or.kr/openApi/restful/prfplc/{hall_id}"
    params = {
        "service": "16d85593b3c94d4c9cb6258b8944cbf3"
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
