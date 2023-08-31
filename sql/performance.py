def insert_performance(connection, performance, seller_id, hall_id):
    cursor = connection.cursor()

    sql = """
        INSERT INTO performance(title, poster_url, start_date, end_date, duration, age_rating, price, category, seller_id, hall_id)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """

    data = (
        performance.get("title"),
        performance.get("poster_url"),
        performance.get("start_date"),
        performance.get("end_date"),
        performance.get("duration"),
        performance.get("age_rating"),
        performance.get("price"),
        performance.get("category"),
        seller_id,
        hall_id
    )

    cursor.execute(sql, data)
    connection.commit()

    return cursor.lastrowid
