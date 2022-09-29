import pytest
import requests
# import base_case


@pytest.fixture()
def login_do():
    print("执行登录操作")
    data = {
        "loginId": "UA244Y8SbzJRKNVluixyKA==",
        "password": "qLpmhT5PIxYdFCh/kZ+dcw=="
    }
    url = "http://**"
    header = {"Connection": "close"}
    re = request_test(url, "POST", data, header)

    # re = requests.post("http://**", data=data)
    # print("login接口返回的结果：")
    # print(re.text)
    # # print(re.headers)
    # print(re.headers['Set-Cookie'])
    setcookie = re.headers['Set-Cookie'].split(";")[0]
    print(re.headers['Set-Cookie'].split(";")[0])
    # return setcookie
    yield setcookie


# @pytest.fixture()
# def login_do_session():
#     print("执行登录操作")
#     data = {
#         "loginId": "UA244Y8SbzJRKNVluixyKA==",
#         "password": "qLpmhT5PIxYdFCh/kZ+dcw=="
#     }
#     url = "http://**"
#     re = request_test_session(url, method="POST",data = data)
#
#     # re = requests.post("http://**", data=data)
#     # print("login接口返回的结果：")
#     # print(re.text)
#     # # print(re.headers)
#     # print(re.headers['Set-Cookie'])
#     setcookie = re.headers['Set-Cookie'].split(";")[0]
#     print(re.headers['Set-Cookie'].split(";")[0])
#     # return setcookie
#     yield


# def request_test_session(url, method, data):
#     session = requests.session()
#     if method == 'GET':
#         re = session.get(url, data=data)
#         print("login接口返回的结果：")
#         print(re.text)
#         # print(re.headers)
#         print(re.headers['Set-Cookie'])
#         setcookie = re.headers['Set-Cookie'].split(";")[0]
#         print(re.headers['Set-Cookie'].split(";")[0])
#         return re
#     elif method == 'POST':
#         re = session.post(url, data=data)
#         print("login接口返回的结果：")
#         print(re.text)
#         # print(re.headers)
#         print(re.headers['Set-Cookie'])
#         setcookie = re.headers['Set-Cookie'].split(";")[0]
#         print(re.headers['Set-Cookie'].split(";")[0])
#         return re
#
#
#
#
def request_test(url,method,data,header):

    if method == 'GET':
        re = requests.get(url, data=data,headers=header)
        print("login接口返回的结果：")
        print(re.text)

        return re
    elif method == 'POST':
        re = requests.post(url, data=data,headers=header)
        print("login接口返回的结果：")
        print(re.text)
        # print(re.headers)

        return  re
