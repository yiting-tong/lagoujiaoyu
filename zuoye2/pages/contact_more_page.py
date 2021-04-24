from part_six.zuoye2.pages.basepage import BasePage
from part_six.zuoye2.pages.edit_information_page import EditInformationPage


class ContactMore(BasePage):
    def edit_information(self):
        self.parse_action("../pages/contact_more.yaml", "edit_information")
        return EditInformationPage(self.driver)
