from python_code.calc import Calculator
import pytest

# @pytest.fixture(scope="class")
# def get_calc():
#     print("获取计算器实例")
#     calc = Calculator()
#     return calc


'''
创建 fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
将 fixture 方法存放在 conftest.py ，设置 scope=module
'''
@pytest.fixture(scope='module')
def dayin():
    print("【开始计算】")
    calc = Calculator()
    yield calc
    print("【计算结束】")
