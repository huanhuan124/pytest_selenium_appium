import pytest


# name_list = ['python','java','php']
# @pytest.mark.parametrize("name",name_list)
# def testname(name):
#     assert name in name_list
#
#
#
# @pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("4+6", 10)], ids=["num1", "num2"])
# def testparam(test_input, expected):
#     assert eval(test_input) == expected
#
#
# @pytest.mark.parametrize("name",["lily",'lisa'])
# @pytest.mark.parametrize("age",[18,20])
# def test_dkerj(name,age):
#     print(name,age)


def test_double1():
    assert 1.2 == 1.2
def test_double2():
    assert 1.0 == 1.0

def test_int1():
    print("int 11111")
    assert 1 == 1

# print(__name__)

#
