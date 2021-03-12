from python_code.calc import Calculator
import pytest
import yaml
import allure
import pytest_ordering

'''
课后作业
补全计算器（加减乘除）的测试用例，编写用例顺序：加-除-减-乘
创建 fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
将 fixture 方法存放在 conftest.py ，设置 scope=module
控制测试用例顺序按照【加-减-乘-除】这个顺序执行
结合 allure 生成本地测试报告
'''

# 取出所有测试数据
with open("./datas/calc.yaml") as f:
    # 导入yaml文件
    total = yaml.safe_load(f)["testcalc"]
    # 取出add-加法的测试数据
    add = total["add"]
    add_datas = add["datas"]
    add_id = add["myid"]
    # 取出div-除法的测试数据
    div = total["div"]
    div_datas = div["datas"]
    div_id = div["myid"]
    # 取出sub-减法的测试数据
    sub = total["sub"]
    sub_datas = sub["datas"]
    sub_id = sub["myid"]
    # 取出mul-乘法的测试数据
    mul = total["mul"]
    mul_datas = mul["datas"]
    mul_id = mul["myid"]


# 获取add-加法的测试数据
@pytest.fixture(params=add_datas, ids=add_id)
def get_add_data(request):
    a_data = request.param
    return a_data


# 获取div-除法的测试数据
@pytest.fixture(params=div_datas, ids=div_id)
def get_div_data(request):
    d_data = request.param
    return d_data


# 获取sub-减法的测试数据
@pytest.fixture(params=sub_datas, ids=sub_id)
def get_sub_data(request):
    s_data = request.param
    return s_data


# 获取mul-乘法的测试数据
@pytest.fixture(params=mul_datas, ids=mul_id)
def get_mul_data(request):
    m_data = request.param
    return m_data


# 计算器测试类
@allure.feature("计算器测试类")
class TestCalc:
    # 加法测试
    # 第1执行
    @allure.story("加法测试")
    @pytest.mark.run(order=1)
    def test_add(self, dayin, get_add_data):
        with allure.step("调用加法计算"):
            add_re = dayin.add(get_add_data[0], get_add_data[1])
        with allure.step("小数rounding问题处理"):
            if isinstance(add_re, float):
                add_re = round(add_re, 2)
        with allure.step("断言判断是否正确"):
            assert add_re == get_add_data[2]

    # 除法测试
    # 第4执行
    @allure.story("除法测试")
    @pytest.mark.run(order=4)
    def test_div(self, dayin, get_div_data):
        with allure.step("调用除法计算"):
            div_re = dayin.div(get_div_data[0], get_div_data[1])
        with allure.step("小数rounding问题处理"):
            if isinstance(div_re, float):
                div_re = round(div_re, 2)
        with allure.step("断言判断是否正确"):
            assert div_re == get_div_data[2]

    # 减法测试
    # 第2执行
    @allure.story("减法测试")
    @pytest.mark.run(order=2)
    def test_sub(self, dayin, get_sub_data):
        with allure.step("调用减法计算"):
            sub_re = dayin.sub(get_sub_data[0], get_sub_data[1])
        with allure.step("小数rounding问题处理"):
            if isinstance(sub_re, float):
                sub_re = round(sub_re, 2)
        with allure.step("断言判断是否正确"):
            assert sub_re == get_sub_data[2]

    # 乘法测试
    # 第3执行
    @allure.story("乘法测试")
    @pytest.mark.run(order=3)
    def test_mul(self, dayin, get_mul_data):
        with allure.step("调用乘法计算"):
            mul_re = dayin.mul(get_mul_data[0], get_mul_data[1])
        with allure.step("小数rounding问题处理"):
            if isinstance(mul_re, float):
                mul_re = round(mul_re, 2)
        with allure.step("断言判断是否正确"):
            assert mul_re == get_mul_data[2]


# terminal执行语句：
'''
pytest test_new_zuoye.py -vs --alluredir=./result/2
allure serve ./result/2

allure generate ./result/2/ -o ./report/2/ --clean
allure open -h 127.0.0.1 -p 8883 ./report/2
'''
