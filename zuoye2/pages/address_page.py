from part_six.zuoye2.pages.add_member_option_page import AddMemberOptionPage
from part_six.zuoye2.pages.basepage import BasePage
from part_six.zuoye2.pages.search_member_page import SearchMember


class AddressPage(BasePage):
    def goto_add_member_option_page(self):
        # self.driver.find_element_by_xpath("//*[@text='添加成员']").click()
        # self.find_click("//*[@text='添加成员']")
        self.parse_action("../pages/address.yaml", "goto_add_member_option_page")
        return AddMemberOptionPage(self.driver)

    def goto_search(self):
        self.parse_action("../pages/address.yaml", "goto_search")
        return SearchMember(self.driver)
