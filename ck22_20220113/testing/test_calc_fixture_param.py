'''
    实战2：
    使用fixture实现参数化
    @pytest.fixture(params=[[1, 1, 3], [-0.01, 0.02, 0.01], [10, 0.02, 10.02]])
    def get_data(request):
        return request.param
    定义执行顺序，顺序为
        先add方法 P1_1 和 P1_2级别的用例
        其次执行P0 级别
        然后执行 相除方法的用例
        最后执行add 方法P2）
        add 用例 （P1_1>P1_2>P0）> div 用例 >  add 用例（P2）、

'''


import allure
import pytest
import logging

# 大类别 feature
# 小类别 story

@allure.feature('计算器测试用例')
class TestCalc:

    # 添加标签 add标签
    @pytest.mark.add
    @pytest.mark.P0
    @pytest.mark.run(order=4)
    @allure.story('P0测试用例')
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
        assert get_data[2] == result

    # 添加标签 add标签
    @pytest.mark.add
    @pytest.mark.P1_1
    # @pytest.mark.run(order=1)
    @pytest.mark.first
    @allure.story('p1_1测试用例')
    @allure.step("这是P1_1的测试步骤")
    def test_add2(self, get_cacl,get_data2):
        """
        【边界】P1:有效边界值相加，结果计算正确
        :return:
        """
        logging.info("加法用例P1_1级别")
        logging.info(f'输入数据：{get_data2[0], get_data2[1]}，预期数据：{get_data2[2]}')
        result = get_cacl.add(get_data2[0], get_data2[1])
        allure.attach.file('C:/Users/zenghuan/PycharmProjects/ck22_20220113/testing/pic/test.jpg', name="测试图片",attachment_type=allure.attachment_type.JPG,extension=".jpg")
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
    @allure.story('p1_2测试用例')
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


    @pytest.mark.run(order=3)
    @allure.story('error测试用例')
    def test_add_error(self, get_cacl, get_error_data):
        a = get_error_data[0]
        b = get_error_data[1]
        expect = get_error_data[2]
        # eval("")将字符串转成对象
        with pytest.raises(eval(expect)) as e:
            result = get_cacl.add(a, b)
        # 断言
        # e.typename 获取断言的类型
        assert expect == e.typename
