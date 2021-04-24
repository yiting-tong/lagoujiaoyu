from part_six.zuoye2.pages.basepage import BasePage
from part_six.zuoye2.pages.contact_more_page import ContactMore


class ContactIndex(BasePage):
    def click_more(self):
        self.parse_action("../pages/contact_index.yaml", "click_more")
        return ContactMore(self.driver)
