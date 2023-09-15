from datetime import date


def insert_customer(connection):
    cursor = connection.cursor()

    sql = """
        INSERT INTO customer(username, password, name, email, birth_date, phone, address)
        VALUES(%s, %s, %s, %s, %s, %s, %s);
    """

    for i in range(1, 101):
        data = (
            f"testCustomer{i}",
            f"${i}b$12$76taFAFPE9ydE0ZsuWkIZexWVjLBbEIRNc509/OLI5nM9d5r3fkRG",
            f"구매자{i}",
            f"testCustomer{i}@ticketparis.com",
            date(1990, 1, 1),
            f"010-1234-5{str(i).zfill(3)}",
            f"경기도 성남시 분당구 정자동 100-{i}"
        )
        cursor.execute(sql, data)

    connection.commit()


def get_customer_ids(connection):
    cursor = connection.cursor()

    sql = """
        SELECT customer_id FROM customer;
    """

    cursor.execute(sql)

    return [row[0] for row in cursor.fetchall()]


def insert_seller(connection):
    cursor = connection.cursor()

    sql = """
        INSERT INTO seller(username, password, name, registration_number, store_name, email, phone)
        VALUES(%s, %s, %s, %s, %s, %s, %s);
    """

    data = (
        'testSeller1',
        '$4b$12$76taFAFPE9ydE0ZsuWkIZexWVjLBbEIRNc509/OLI5nM9d5r3fkRG',
        '판매자1',
        '100-12-56789',
        '주식회사 티켓파리',
        'testSeller1@ticketparis.com',
        '010-4234-1674'
    )

    cursor.execute(sql, data)
    connection.commit()

    return cursor.lastrowid
