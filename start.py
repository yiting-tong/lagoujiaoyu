'''
原有存款1000元，发工资之后存款变为2000元
定义模块：
1.money.py saved_money=1000
2.定义发工资模块 send_money,用来增加收入计算
3.定义工资查询模块select_money,用来展示工资数额
4.定义一个start.py,启动文件展示最终存款金额
ceshiren.com/t/topic/8381
'''

from send_money import send_money
from select_money import select_money


if __name__ == "__main__":
    send_money(2000)
    select_money()
