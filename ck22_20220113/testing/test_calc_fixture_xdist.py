'''
    实战3：
    加速执行，三个进程并发执行所有用例
    生成测试报告，添加用例分类
    添加测试步骤，添加图像（本地图片）


'''
from time import sleep

import allure
import pytest
import logging

# 大类别 feature
# 小类别 story


class TestCalc:

    # 添加标签 add标签
    @pytest.mark.add
    @pytest.mark.P0
    @pytest.mark.run(order=4)
    # @pytest.mark.parametrize("a,b,expect", [[1, 1, 3], [-0.01, 0.02, 0.01], [10, 0.02, 10.02]])
    # def test_add1(self, get_cacl, a, b, expect):

    def test_add1(self, get_cacl,get_data):
        """
        【正向】P0 :2个整数相加，结果计算正确
        :return:
        """
        logging.info("加法用例P0级别")
        logging.info(f'输入数据：{get_data[0],get_data[1]}，预期数据：{get_data[2]}')
        result = get_cacl.add(get_data[0], get_data[1])
        sleep(1)
        assert get_data[2] == result

    # 添加标签 add标签
    @pytest.mark.add
    @pytest.mark.P1_1
    # @pytest.mark.run(order=1)
    @pytest.mark.first
    def test_add2(self, get_cacl,get_data2):
        """
        【边界】P1:有效边界值相加，结果计算正确
        :return:
        """
        logging.info("加法用例P1_1级别")
        logging.info(f'输入数据：{get_data2[0], get_data2[1]}，预期数据：{get_data2[2]}')
        result = get_cacl.add(get_data2[0], get_data2[1])
        sleep(1)
        assert get_data2[2] == result

    @pytest.mark.add
    @pytest.mark.P1_2
    @pytest.mark.parametrize("a,b,expect", [
        [99.01, 0, "参数大小超出范围"],
        [-99.01, -1, "参数大小超出范围"],
        [2, 99.01, "参数大小超出范围"],
        [1, -99.01, "参数大小超出范围"]
    ])
    @pytest.mark.run(order=2)
    def test_add3(self, get_cacl, a, b, expect):
        """
        【边界】P1:无效边界值相加，给出提示信息
        :return:
        """
        logging.info("加法用例P1_2级别")
        logging.info(f'输入数据：{a, b}，预期数据：{expect}')
        sleep(1)
        with allure.step("步骤一：执行相加操作"):
            result = get_cacl.add(a, b)
        # 断言
        with allure.step("步骤二：断言"):
            allure.attach.file("/Users/juanxu/Downloads/logo.jpg",
                               name="图片",
                               attachment_type=allure.attachment_type.JPG,
                               extension=".jpg")
            assert expect == 2


    @pytest.mark.run(order=3)
    def test_add_error(self, get_cacl, get_error_data):
        a = get_error_data[0]
        b = get_error_data[1]
        expect = get_error_data[2]
        # eval("")将字符串转成对象
        sleep(1)
        with pytest.raises(eval(expect)) as e:
            result = get_cacl.add(a, b)
        # 断言
        # e.typename 获取断言的类型
        assert expect == e.typename
