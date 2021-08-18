from configparser import ConfigParser

import psycopg2
import json

def config(filename='database.ini', section='postgres'):
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')

    return db


""" create tables in the PostgreSQL database"""
commands = (
    """
        CREATE TABLE vendors (
            vendor_id SERIAL PRIMARY KEY,
            vendor_name VARCHAR(255) NOT NULL
        )
    """,
    """
    SELECT * from vendors
    """,
    """
    INSERT INTO vendors (vendor_name) VALUES ('some-vendor-new')
    """,
    """
    SELECT * from test_js
    """,
)


def connect(command=None):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        if not command:
            command = 'SELECT version()'
        cur.execute(command)
        conn.commit()
        result = []
        row = cur.fetchone()
        while row is not None:
            print(row, 'xxxx')
            result.append(row)
            row = cur.fetchone()
        cur.close()
        return result

    except (Exception, psycopg2.DatabaseError) as exc:
        print(exc)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

dic = [{"1": "test", "2" : "test 33333"}]
my_json = dic
my_json = json.dumps(dic)

print(my_json)
# command = """INSERT INTO test (js) VALUES ('[{"a":"foo"},{"b":"bar"},{"c":"baz"}]')"""
command = f"INSERT INTO test_js (js) VALUES ('{my_json}')"
print(command)
if __name__ == '__main__':
    params = config()
    print(params)
    connect(command=command)
    # res = connect(command=commands[3])
    # for line in res:
    #     js = line[1][0]
    #     print(js, type(js))
    #     # js = json.loads(js)
    #     # print(js, type(js))
# TABLE_NAME = 'json_input'
# TABLE_COLUMN = 'js_data'
# PARAMS = {
#     'host': 'localhost',
#     'database': 'PG_TEST',
#     'user': 'postgres',
#     'password': '20003000'
# }
#
#
# def config(filename='database.ini', section='postgres'):
#     parser = ConfigParser()
#     parser.read(filename)
#     db = {}
#     if parser.has_section(section):
#         params = parser.items(section)
#         for param in params:
#             db[param[0]] = param[1]
#     else:
#         raise Exception(f'Section {section} not found in the {filename} file')
#
#     return db
#
#
# def write_js_to_db(json):
#     conn = None
#     try:
#         # params = config()
#         params = PARAMS
#         conn = psycopg2.connect(**params)
#         cur = conn.cursor()
#         command = f"INSERT INTO {TABLE_NAME} ({TABLE_COLUMN}) VALUES ('{json}')"
#         cur.execute(command)
#         conn.commit()
#         cur.close()
#     except (Exception, psycopg2.DatabaseError) as exc:
#         print(exc)
#     finally:
#         if conn is not None:
#             conn.close()
#             print('Database connection closed.')
#
#
# def get_all_data():
#     conn = None
#     result = []
#     try:
#         # params = config()
#         params = PARAMS
#         conn = psycopg2.connect(**params)
#         cur = conn.cursor()
#         command = f"SELECT * FROM {TABLE_NAME}"
#         cur.execute(command)
#         row = cur.fetchone()
#         while row:
#             result.append(row)
#             row = cur.fetchone()
#         cur.close()
#     except (Exception, psycopg2.DatabaseError) as exc:
#         print(exc)
#     finally:
#         if conn is not None:
#             conn.close()
#             print('Database connection closed.')
#         return result