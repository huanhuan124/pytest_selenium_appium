'''
    实战1：
    使用fixture 提供 calc 对象
    使用 fixture实现：用例执行之前打印【开始计算】，之后【结束计算】
    当前模块所有用例执行完成之后，打印【测试结束】
    每条用例添加测试日志，并将日志打印输出到logs/ <日期_时间>.log 文件中


'''


import allure
import pytest
import logging

# 大类别 feature
# 小类别 story


class TestCalc:

    # 添加标签 add标签
    @pytest.mark.add
    @pytest.mark.P0
    @pytest.mark.parametrize("a,b,expect", [[1, 1, 3], [-0.01, 0.02, 0.01], [10, 0.02, 10.02]])
    def test_add1(self, get_cacl, a, b, expect):
        """
        【正向】P0 :2个整数相加，结果计算正确
        :return:
        """
        logging.info("加法用例P0级别")
        logging.info(f'输入数据：{a,b}，预期数据：{expect}')
        result = get_cacl.add(a, b)
        assert expect == result

    # 添加标签 add标签
    @pytest.mark.add
    @pytest.mark.P1_1
    @pytest.mark.parametrize("a,b,expect", [[98.99, 99, 197.99], [99, 98.99, 197.99],
        [-98.99, -99, -197.99], [-99, -98.99, -197.99]])
    def test_add2(self, get_cacl,a, b, expect):
        """
        【边界】P1:有效边界值相加，结果计算正确
        :return:
        """
        logging.info("加法用例P1_1级别")
        logging.info(f'输入数据：{a, b}，预期数据：{expect}')
        result = get_cacl.add(a, b)
        assert expect == result

    @pytest.mark.add
    @pytest.mark.P1_2
    @pytest.mark.parametrize("a,b,expect", [
        [99.01, 0, "参数大小超出范围"],
        [-99.01, -1, "参数大小超出范围"],
        [2, 99.01, "参数大小超出范围"],
        [1, -99.01, "参数大小超出范围"]
    ])
    def test_add3(self, get_cacl, a, b, expect):
        """
        【边界】P1:无效边界值相加，给出提示信息
        :return:
        """
        logging.info("加法用例P1_2级别")
        logging.info(f'输入数据：{a, b}，预期数据：{expect}')
        with allure.step("步骤一：执行相加操作"):
            result = get_cacl.add(a, b)
        # 断言
        with allure.step("步骤二：断言"):
            allure.attach.file("/Users/juanxu/Downloads/logo.jpg",
                               name="图片",
                               attachment_type=allure.attachment_type.JPG,
                               extension=".jpg")
            assert expect == 2


    # def test_add_error(self, get_cacl, get_error_data):
    #     a = get_error_data[0]
    #     b = get_error_data[1]
    #     expect = get_error_data[2]
    #     # eval("")将字符串转成对象
    #     with pytest.raises(eval(expect)) as e:
    #         result = get_cacl.add(a, b)
    #     # 断言
    #     # e.typename 获取断言的类型
    #     assert expect == e.typename
