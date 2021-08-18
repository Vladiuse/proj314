import psycopg2


def create_table():
    params = {
        'host': 'localhost',
        'database': 'PG_TEST',
        'user': 'postgres',
        'password': '20003000'
    }
    command = 'CREATE TABLE json_input ' \
              '(js_id BIGSERIAL PRIMARY KEY, js_data JSONB NOT NULL)'

    conn = None
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(command)
        conn.commit()
        cur.close()
        print('Table created')
    except (Exception, psycopg2.DatabaseError) as exc:
        print(exc)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def run():
    create_table()
