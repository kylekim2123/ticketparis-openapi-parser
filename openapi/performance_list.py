import requests
from bs4 import BeautifulSoup

from openapi.performance_detail import get_performance_detail


def get_performance_list(start_page, rows):
    url = "http://kopis.or.kr/openApi/restful/pblprfr"
    params = {
        "service": "16d85593b3c94d4c9cb6258b8944cbf3",
        "stdate": 20230801,
        "eddate": 20230930,
        "cpage": start_page,
        "rows": rows
    }

    response = requests.get(url, params)
    dbs = BeautifulSoup(response.content, "lxml")
    data = []

    for db in dbs.find_all("db"):
        performance_id = db.mt20id.text.strip()
        data.append(get_performance_detail(performance_id))

    return data


def select_hall(cursor, name):
    sql = """
        SELECT performance_id FROM hall WHERE name = %s;
    """

    data = (name,)

    cursor.execute(sql, data)
    return cursor.fetchone()[0]