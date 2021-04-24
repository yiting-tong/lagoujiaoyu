from part_six.zuoye2.pages.app import App


class TestAddMember:
    def setup(self):
        self.app = App()

    def test_delete_member(self):
        search_name = "aaa14"
        department = "测试"
        middle_page = self.app.goto_main().goto_address_page().goto_search().search_member(search_name)
        middle_page.choose_member(department).click_more().edit_information().delet_member().delete_confirm()
        middle_page.verify_delete()
