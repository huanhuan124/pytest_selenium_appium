from selenium import webdriver

from 第三方库.数据库 import get_conn


class Test_demo_db_setup:


    def setup_class(self):
        # 1、建立连接
        self.conn = get_conn()
        # 2、获取游标
        self.cursor = self.conn.cursor()




    def teardown_class(self):
        # 5、关闭连接
        self.conn.close()



    def test_create(self):

        create_sql = "create table testcase2 (id int(11) not null auto_increment primary key ,title varchar(255) not null, owner varchar(255) not null )"
        # 3、执行SQL
        self.cursor.execute(create_sql)


    def test_insert(self):

        insert_sql = "insert into testcase2 (id,title,owner) values (3,'第3个用例','zenghuan3')"
        try:
            # 执行sql
            self.cursor.execute(insert_sql)
            # 提交
            self.conn.commit()
        except:

            #发生异常时进行回滚
            self.conn.rollback()
        finally:
            #关闭连接
            # conn.close()
            print("已关闭")




