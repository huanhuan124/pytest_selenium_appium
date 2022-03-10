import yaml


def test_yml():
    #C:\Users\zenghuan\PycharmProjects\test_selenium_appium\wework_po\datas\datas

    with open("C:/Users/zenghuan/PycharmProjects/test_selenium_appium/wework_po/datas/datas.yml", 'r',encoding='utf-8') as f:
        result = yaml.safe_load(f)
    print(result)
    print(result.get("datas"))
