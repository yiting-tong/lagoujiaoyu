from part_six.zuoye2.pages.basepage import BasePage


class AddMemberPage(BasePage):

    def add_member(self):
        # self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/ays']").send_keys("aaa07")
        # self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/f4m']").send_keys("12341234007")
        # self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/ac9']").click()

        # self.find_send_keys("//*[@resource-id='com.tencent.wework:id/ays']", "aaa08")
        # self.find_send_keys("//*[@resource-id='com.tencent.wework:id/f4m']", "12341234008")
        # self.find_click("//*[@resource-id='com.tencent.wework:id/ac9']")
        self.parse_action("../pages/add_member.yaml", "add_member")
