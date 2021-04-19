from part_six.zuoye1.pages.app import App


class TestAddMember:
    def setup(self):
        self.app = App()

    def test_add_member(self):
        self.app.goto_main().goto_address_page().goto_add_member_option_page().goto_add_member_page().add_member()
