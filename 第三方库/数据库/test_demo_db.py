from 第三方库.数据库 import get_conn
import pytest

# 1、检查命名格式是否规范
#
#     .py文件必须以test_开头（或者_test结尾）
#     测试类必须以Test开头，且不能有init方法
#     测试方法必须以test_开头
#     断言必须用assert
# 2、.py文件是否改过名字
# 分享刚踩的坑：如图
# 文件以及函数命名都符合规范，但是运行就是提示collected 0 items，百思不得其解，百度N次后，终于解决。
# 原因：修改过文件名。文件写好后，修改文件名的话，后续的代码无法记录到此文件中，所以需要把代码重新写一遍（重新copy应该也行），注意下次建文件时，最好名字一次到位，后续不要随意改动。重新写后，就可以正常运行啦。
# ————————————————
# 版权声明：本文为CSDN博主「比丢大人biu～」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/qq_35708058/article/details/112757702

class Test_demo_db:


    def test_create(self,get_db):
        conn, cursor = get_db
        create_sql = "create table testcase2 (id int(11) not null auto_increment primary key ,title varchar(255) not null, owner varchar(255) not null )"
        # 3、执行SQL
        cursor.execute(create_sql)


    def test_insert(self, get_db):
        conn, cursor = get_db
        insert_sql = "insert into testcase2 (id,title,owner) values (3,'第3个用例','zenghuan3')"
        try:
            # 执行sql
            cursor.execute(insert_sql)
            # 提交
            conn.commit()
        except:
            # 发生异常时进行回滚
            conn.rollback()
        finally:
            # 关闭连接
            print("关闭成功")
            # conn.close()

if __name__ == '__main__':
    # pytest.main(["-v", "-s", "test_demo_db.py"])
    pytest.main()