
import jsonpath


def test_json():
    a=[{'method': 'get', 'param': {'mobile': '+8618207102348'}, 'url': 'https://platform-auth-center-test.rockeyops.com/sms/sendVerificationCode', 'title': '发送国内验证码'}, {'method': 'get', 'param': {'mobile': '+8618207102347'}, 'url': 'https://platform-auth-center-test.rockeyops.com/sms/sendVerificationCode', 'title': '发送国外验证码'}]

    title = jsonpath.jsonpath(a,'$..title')
    print(title)

    b = [i.get("title") for i in a]
    print(b)