def insert_hall(connection, hall):
    cursor = connection.cursor()

    sql = """
        INSERT IGNORE INTO hall(name, address, seats_count)
        VALUES(%s, %s, %s);
    """

    data = (
        hall.get("name"),
        hall.get("address"),
        hall.get("seats_count")
    )

    cursor.execute(sql, data)
    connection.commit()

    sql = """
        SELECT hall_id FROM hall WHERE name = %s;
    """

    data = (hall.get("name"),)

    cursor.execute(sql, data)

    return cursor.fetchone()[0]
