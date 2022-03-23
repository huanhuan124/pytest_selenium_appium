from 第三方库.数据库 import get_conn


# class test_db:


# def setup_method():
#         # 1、建立连接
#         conn = get_conn()
#         # 2、获取游标
#         cursor = conn.cursor()
#
#
# def teardown_method():
#         # 5、关闭连接
#
#         conn.close()


def test_conn():
    # 1、建立连接
    conn = get_conn()
    # 2、获取游标
    cursor = conn.cursor()
    # 3、执行SQL
    cursor.execute("SELECT VERSION();")
    # 4、获取结果
    version = cursor.fetchone()
    print(version)
    # 5、关闭连接
    conn.close()


def test_create():
    # 1、建立连接
    conn = get_conn()
    # 2、获取游标
    cursor = conn.cursor()
    create_sql = "create table testcase (id int(11) not null auto_increment primary key ,title varchar(255) not null, owner varchar(255) not null )"
    # 3、执行SQL
    cursor.execute(create_sql)
    # 4、关闭连接
    conn.close()

def test_insert():
    conn = get_conn()
    cursor = conn.cursor()
    insert_sql = "insert into testcase (id,title,owner) values (3,'第3个用例','zenghuan3')"
    try:
        # 执行sql
        cursor.execute(insert_sql)
        # 提交
        conn.commit()
    except:
        #发生异常时进行回滚
        conn.rollback()
    finally:
        #关闭连接
        conn.close()

def test_select():
    conn = get_conn()
    cursor = conn.cursor()
    select_sql = "select *  from testcase"
    cursor.execute(select_sql)
    result = cursor.fetchall()
    print(result)
    conn.close()

def test_update():
    conn = get_conn()
    cursor = conn.cursor()
    update_sql = "update testcase set title = '第1个用例' where id =1"
    try:
        # 执行sql
        cursor.execute(update_sql)
        # 提交
        conn.commit()
    except:
        # 发生异常时进行回滚
        conn.rollback()
    finally:
        # 关闭连接
        conn.close()


def test_delete():
    conn = get_conn()
    cursor = conn.cursor()
    delete_sql = "delete from  testcase  where id =1"
    try:
        # 执行sql
        cursor.execute(delete_sql)
        # 提交
        conn.commit()
    except:
        # 发生异常时进行回滚
        conn.rollback()
    finally:
        # 关闭连接
        conn.close()


