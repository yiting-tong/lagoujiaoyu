from part_six.zuoye2.pages.basepage import BasePage


class EditInformationPage(BasePage):
    def delet_member(self):
        self.parse_action("../pages/edit_information.yaml", "delet_member")
        return self

    def delete_confirm(self):
        self.parse_action("../pages/edit_information.yaml", "delete_confirm")
