# 添加联系人PO
# 1.输入信息，点击保存，返回通讯录页
# 2.输入信息，点击取消未保存，返回通讯录页
# 2.输入信息，点击保存并继续添加，返回添加联系人页
from time import sleep

from selenium.webdriver.common.by import By

from part_five.zuoye1.page.base import Base


class AddMember(Base):

    # 点击保存，返回通讯录页
    def add_member_save(self, username, account, phone):
        self.find(By.ID, "username").send_keys(username)
        self.find(By.ID, "memberAdd_acctid").send_keys(account)
        self.find(By.ID, "memberAdd_phone").send_keys(phone)
        self.find(By.XPATH, "//form[@class='js_member_editor_form']/div[1]/a[2]").click()
        return True

    # 点击取消未保存，返回通讯录页
    def add_member_cancel(self, username, account, phone):
        self.find(By.ID, "username").send_keys(username)
        self.find(By.ID, "memberAdd_acctid").send_keys(account)
        self.find(By.ID, "memberAdd_phone").send_keys(phone)
        self.find(By.XPATH, "//form[@class='js_member_editor_form']/div[1]/a[3]").click()
        self.find(By.XPATH, "//div[@class='qui_dialog_foot ww_dialog_foot']/a[2]").click()
        return True

    def add_member_continue(self, username, account, phone):
        self.find(By.ID, "username").send_keys(username)
        self.find(By.ID, "memberAdd_acctid").send_keys(account)
        self.find(By.ID, "memberAdd_phone").send_keys(phone)
        self.find(By.XPATH, "//form[@class='js_member_editor_form']/div[1]/a[1]").click()
        return AddMember(self._driver)
