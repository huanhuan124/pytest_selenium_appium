import pymysql


def get_conn():
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='123456',
        database='uc_db',
        charset='utf8mb4')
    return conn
