from part_six.zuoye1.pages.add_member_option_page import AddMemberOptionPage
from part_six.zuoye1.pages.basepage import BasePage


class AddressPage(BasePage):
    def goto_add_member_option_page(self):
        # self.driver.find_element_by_xpath("//*[@text='添加成员']").click()
        # self.find_click("//*[@text='添加成员']")
        self.parse_action("../pages/address.yaml")
        return AddMemberOptionPage(self.driver)
