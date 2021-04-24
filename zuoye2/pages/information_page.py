from part_six.zuoye2.pages.address_page import AddressPage
from part_six.zuoye2.pages.basepage import BasePage


class InformationPage(BasePage):

    def goto_address_page(self):
        # self.driver.find_element_by_xpath("//*[@text='通讯录']").click()
        # self.find_click("//*[@text='通讯录']")
        self.parse_action("../pages/information.yaml", "goto_address_page")
        return AddressPage(self.driver)
