import time

import pytest

from pythoncode.calculator import Calculator


@pytest.fixture(autouse=True)
def start():
    # 每条测试用例之前调用
    print("开始计算")
    # 每条用例执行之后 被调用
    print("结束计算")




@pytest.fixture(scope='session')
def get_cacl():
    calc = Calculator()
    yield calc
    print("===========>结束测试")


'''
生成log文件，以当前时间为文件名
设置了这个以后，pytest.ini文件中设置的log文件名就失效了
'''
@pytest.fixture(scope="session", autouse=True)
def manage_logs(request):
    """Set log file name same as test name"""
    now = time.strftime("%Y%m%d_%H%M%S")
    log_name = './log/' + now + '.log'

    request.config.pluginmanager.get_plugin("logging-plugin") \
        .set_log_path(log_name)

#fixture参数化
@pytest.fixture(params=[[1, 1, 3], [-0.01, 0.02, 0.01], [10, 0.02, 10.02]])
def get_data(request):
    return request.param


#fixture参数化
@pytest.fixture(params=[[98.99, 99, 197.99], [99, 98.99, 197.99],
        [-98.99, -99, -197.99], [-99, -98.99, -197.99]])
def get_data2(request):
    return request.param