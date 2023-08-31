import requests
from bs4 import BeautifulSoup
from decouple import config

from openapi.hall_detail import get_hall_detail
from openapi.utils import (
    switch_age,
    switch_genre,
    switch_date,
    parse_price,
    parse_sequence_times
)


def get_performance_detail(performance_id):
    url = f"http://kopis.or.kr/openApi/restful/pblprfr/{performance_id}"
    params = {
        "service": config("API_KEY")
    }

    response = requests.get(url, params)
    db = BeautifulSoup(response.content, "lxml")

    return {
        "title": db.prfnm.text.strip(),
        "poster_url": db.poster.text.strip(),
        "start_date": switch_date(db.prfpdfrom.text.strip()),
        "end_date": switch_date(db.prfpdto.text.strip()),
        "category": switch_genre(db.genrenm.text.strip()),
        "duration": db.prfruntime.text.strip(),
        "age_rating": switch_age(db.prfage.text.strip()),
        "price": parse_price(db.pcseguidance.text.strip()),
        "sequences": parse_sequence_times(db.dtguidance.text.strip()),
        "hall": get_hall_detail(db.mt10id.text.strip())
    }
