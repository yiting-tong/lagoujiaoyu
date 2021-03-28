# 通讯录PO
# 1.点击添加成员，返回添加成员页
# 2.检查所有成员姓名
from time import sleep

from selenium.webdriver.common.by import By

from part_five.zuoye1.page.add_member import AddMember
from part_five.zuoye1.page.base import Base


class Contact(Base):

    # 点击添加成员，返回添加成员页
    def goto_add_member(self):
        # 强制等待1s，解决raise exception_class(message, screen, stacktrace)报错
        sleep(1)
        self.find(By.XPATH, "/html/body/div[1]/div/div/main/div/div/div[2]/div/div[2]/div[3]/div[1]/a[1]").click()
        return AddMember(self._driver)

    # 检查所有成员姓名
    def get_member(self):
        sleep(1)
        locator = (By.CSS_SELECTOR, '.member_colRight_memberTable_th_Checkbox')
        self.wait(10, locator)
        ele_list = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        name_list = []
        for ele in ele_list:
            name_list.append(ele.get_attribute("title"))
        return name_list
