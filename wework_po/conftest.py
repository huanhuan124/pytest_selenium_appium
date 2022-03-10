'''
生成log文件，以当前时间为文件名
设置了这个以后，pytest.ini文件中设置的log文件名就失效了
'''
import time

import pytest


@pytest.fixture(scope="session", autouse=True)
def manage_logs(request):
    """Set log file name same as test name"""
    '''
    生成log文件，以当前时间为文件名
    设置了这个以后，pytest.ini文件中设置的log文件名就失效了
    '''

    now = time.strftime("%Y%m%d_%H%M%S")
    log_name = './log/' + now + '.log'
    request.config.pluginmanager.get_plugin("logging-plugin") \
        .set_log_path(log_name)

def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")

