import pytest

test_user_data = ['tom', 'jelly']
@pytest.fixture()
def login(request):
    user = request.param
    print(f'登录用户是：{user}')
    return user

@pytest.mark.parametrize("login", test_user_data, indirect=True)
def test_login(login):
    # a = login
    print(f'测试用例中login的返回值是：{login}')
    assert login in test_user_data


# @pytest.fixture()
# def login():
#     print("这是登录方法，需要先登录")
#
# def test_cart(login):
#     print("下单")
