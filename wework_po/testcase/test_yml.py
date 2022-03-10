import os.path

import yaml


def test_yml():
    #表示当前所处的文件夹的绝对路径
    print(os.path.abspath('.'))
    # 表示当前所处的文件夹上一级文件夹的绝对路径
    print(os.path.abspath('..'))

    #C:\Users\zenghuan\PycharmProjects\test_selenium_appium\wework_po\datas\datas
    print(os.path.abspath('./datas'))

    # with open("C:/Users/zenghuan/PycharmProjects/test_selenium_appium/wework_po/datas/datas.yml", 'r',encoding='utf-8') as f:
    # 使用相对路径读取yaml文件
    with open("../datas/datas.yml", 'r',encoding='utf-8') as f:
        result = yaml.safe_load(f)
    print(result)
    print(result.get("datas"))
