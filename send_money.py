'''
定义发工资模块 send_money,用来增加收入计算
'''

import money


def send_money(add):
    add_money = add
    money.money = money.money + add_money
    print(f"本次存入{add_money}元")

if __name__ == "__main__":
    send_money(1000)