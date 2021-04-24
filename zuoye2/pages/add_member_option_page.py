from part_six.zuoye2.pages.add_member_page import AddMemberPage
from part_six.zuoye2.pages.basepage import BasePage


class AddMemberOptionPage(BasePage):
    def goto_add_member_page(self):
        # self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()
        # self.find_click("//*[@text='手动输入添加']")
        self.parse_action("../pages/add_member_option.yaml", "goto_add_member_page")
        return AddMemberPage(self.driver)
