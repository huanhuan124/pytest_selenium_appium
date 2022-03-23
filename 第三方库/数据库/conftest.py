import pytest

from 第三方库.数据库 import get_conn


@pytest.fixture()
def get_db():
    print("lianjie")
    # 1、建立连接
    conn = get_conn()
    # 2、获取游标
    cursor = conn.cursor()
    yield conn,cursor
    # 4、关闭连接
    conn.close()
    print("closed")