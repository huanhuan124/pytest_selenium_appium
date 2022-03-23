


# from 普通功能.testcase.nosession import testdemo
from 普通功能.testcase.nosession.testdemo import testa,test_demo,hello

# from 普通功能.testcase.nosession.testdemo import *


def test_b():
        print("bbbbbbb")
        #test_a是类里面的函数
        testa().test_a()
        # print(test_demo.demo)
        #类变量
        print(test_demo.demo)
        #文件里面的变量
        print(hello)
        # a = testa()
        # a.test_a()
        # testa.test_a()
        # testdemo.testa.test_a()
        # testa.test_a()

