import random
from itertools import combinations

from sql.customer_seller import get_customer_ids
from sql.schedule import count_seats, update_schedule_seat_counts


def insert_reservations(connection, schedule_id_list):
    cursor = connection.cursor()

    sql = """
        INSERT INTO reservation(status, customer_id, schedule_id)
        VALUES(%s, %s, %s);
    """

    customer_ids = get_customer_ids(connection)

    for case in combinations(customer_ids, 98):
        for customer_id in case:
            schedule_id = random.choice(schedule_id_list)  # 스케줄 무작위로 하나 뽑기
            seats_count = count_seats(connection, schedule_id)

            if seats_count <= 20:
                continue

            data = (
                "BOOKED",
                customer_id,
                schedule_id
            )

            cursor.execute(sql, data)
            update_schedule_seat_counts(connection, seats_count - 1, schedule_id)
            connection.commit()
