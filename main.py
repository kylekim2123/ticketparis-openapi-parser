import pymysql
from decouple import config

from openapi.performance_list import get_performance_list
from sql.customer_seller import insert_customer, insert_seller
from sql.hall import insert_hall
from sql.performance import insert_performance
from sql.reservation import insert_reservations
from sql.schedule import insert_schedule

MYSQL_ROOT_PASSWORD = config("MYSQL_ROOT_PASSWORD")
DATABASE_NAME = config("DATABASE_NAME")

connection = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password=MYSQL_ROOT_PASSWORD,
    db=DATABASE_NAME,
    charset="utf8"
)

schedule_id_list = []
performance_len = 0

# 1. 구매자, 판매자 데이터 삽입
insert_customer(connection)
seller_id = insert_seller(connection)

for i in range(1, 6):
    for performance in get_performance_list(start_page=i, rows=100):
        hall = performance.get("hall")
        hall_id = insert_hall(connection, hall)  # 2. 공연장 데이터 삽입

        performance_id = insert_performance(connection, performance, seller_id, hall_id)  # 3. 공연 데이터 삽입

        schedule = {
            "start_date": performance.get("start_date"),
            "end_date": performance.get("end_date"),
            "sequences": performance.get("sequences")
        }

        schedule_ids = insert_schedule(connection, schedule, performance_id, hall.get("seats_count"))  # 4. 스케줄 데이터 삽입
        schedule_id_list.extend(schedule_ids)
        performance_len += 1

        # pprint(performance)
        # print()

insert_reservations(connection, schedule_id_list)

connection.close()

print(f"가져온 공연 갯수 = {performance_len}")
print(f"생성된 스케줄 갯수 = {len(schedule_id_list)}")
