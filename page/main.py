# 首页PO
# 1.点击添加成员，进入添加成员页
# 2.点击通讯录，进入通讯录页
from time import sleep

from selenium.webdriver.common.by import By

from part_five.zuoye1.page.add_member import AddMember
from part_five.zuoye1.page.base import Base
from part_five.zuoye1.page.contact import Contact


class Main(Base):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_add_member(self):
        self.find(By.XPATH, "//div[@class='index_service_cnt js_service_list']/a[1]/div[1]/span[2]").click()
        return AddMember(self._driver)

    def goto_contact(self):
        sleep(1)
        self.find(By.XPATH, "//a[@id='menu_contacts']/span").click()
        return Contact(self._driver)
