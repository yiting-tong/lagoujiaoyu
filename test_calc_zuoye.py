import pytest
from python_code.calc import Calculator
import yaml

'''
作业要求:
补全计算器中加法和除法的测试用例
使用参数化完成测试用例的自动生成
在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
注意：
使用等价类，边界值，因果图等设计测试用例
测试用例中添加断言，验证结果
灵活使用 setup(), teardown() , setup_class(), teardown_class()
'''

# 打开yaml文件
with open('./datas/calc.yaml', encoding='utf-8') as f:
    # 取出所有数据
    totaldata = yaml.safe_load(f)["testcalc"]
    print(totaldata)
    # 取出add数据
    add = totaldata["add"]
    # 取出add中测试数据
    add_datas = add["datas"]
    # 取出add中用例重命名数据
    add_id = add["myid"]

    # 取出div数据
    div = totaldata["div"]
    # 取出div中测试数据
    div_datas = div['datas']
    # 取出div中用例重命名数据
    div_id = div['myid']


class TestCalc:
    # setupclass方法，在类开始时创建Calculator实例
    def setup_class(self):
        self.calc = Calculator()

    # 在每个测试用例执行前打印【开始计算】
    def setup(self):
        print('【开始计算】')

    # 在每个测试用例执行后打印【计算结束】
    def teardown(self):
        print('【计算结束】')

    # 将add的测试数据传入测试用例中
    @pytest.mark.parametrize('a,b,expect', add_datas, ids=add_id)
    def test_add(self, a, b, expect):
        # 调用calc的add方法，计算a+b
        result = self.calc.add(a, b)
        # 判断result是否为小数，若是则做round处理
        if isinstance(result, float):
            result = round(result, 2)
        # 用断言判断测试结果是否正确
        assert result == expect

    # 将div的测试数据传入测试用例中
    @pytest.mark.parametrize('a1,b1,except1', div_datas, ids=div_id)
    def test_div(self, a1, b1, except1):
        # 调用calc的div方法，计算a1/b1
        result1 = self.calc.div(a1, b1)
        # 判断result1是否为小数，若是则做round处理
        if isinstance(result1, float):
            result1 = round(result1, 2)
        # 用断言判断测试结果是否正确
        assert result1 == except1
