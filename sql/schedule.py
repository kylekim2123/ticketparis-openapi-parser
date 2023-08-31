from datetime import datetime, timedelta, time


def insert_schedule(connection, schedule, performance_id, seats_count):
    cursor = connection.cursor()

    sql = """
        INSERT INTO schedule(start_datetime, sequence, seats_count, performance_id)
        VALUES(%s, %s, %s, %s);
    """

    start_date = schedule.get("start_date")
    end_date = schedule.get("end_date")
    sequences = [sequence.split(":") for sequence in schedule.get("sequences")]
    schedule_ids = []

    for n in range((end_date - start_date).days + 1):
        date = start_date + timedelta(days=n)

        for i, sequence in enumerate(sequences):
            hour, minute = map(int, sequence)
            start_datetime = datetime.combine(date, time(hour, minute))

            data = (
                start_datetime,
                i + 1,
                seats_count,
                performance_id
            )

            cursor.execute(sql, data)
            connection.commit()

            schedule_ids.append(cursor.lastrowid)

    return schedule_ids


def count_seats(connection, schedule_id):
    cursor = connection.cursor()

    sql = """
        SELECT seats_count FROM schedule WHERE schedule_id = %s;
    """

    data = (schedule_id,)

    cursor.execute(sql, data)
    return cursor.fetchone()[0]


def update_schedule_seat_counts(connection, seats_count, schedule_id):
    cursor = connection.cursor()

    sql = """
        UPDATE schedule SET seats_count = %s WHERE schedule_id = %s;
    """

    data = (seats_count, schedule_id)

    cursor.execute(sql, data)