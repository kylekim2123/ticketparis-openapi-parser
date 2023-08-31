import re
from datetime import datetime


def switch_age(string_age):
    if "세" not in string_age:
        return 0
    result = [s for s in string_age if s.isdecimal()]
    return int("".join(result))


def switch_genre(original_genre):
    genre_table = {
        "뮤지컬": "뮤지컬",
        "대중음악": "콘서트",
        "연극": "연극",
        "무용": "클래식/무용",
        "대중무용": "클래식/무용",
        "서양음악(클래식)": "클래식/무용",
        "한국음악(국악)": "클래식/무용",
        "무용(서양/한국무용)": "클래식/무용",
        "서커스/마술": "전시/행사",
        "복합": "전시/행사",
        "아동": "아동/가족"
    }
    return genre_table.get(original_genre, "기타")


def switch_date(original_date):
    return datetime.strptime(original_date, "%Y.%m.%d").date()


def parse_price(original_price):
    result = [s for s in original_price.split("원")[0] if s.isdecimal()]
    if not result:
        return 10000
    return int("".join(result))


def parse_sequence_times(original_sequence):
    times = sorted(set(re.findall(r"\d{2}:\d{2}", original_sequence)))
    return times
