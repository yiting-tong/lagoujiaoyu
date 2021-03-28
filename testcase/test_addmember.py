# test_addmember
from time import sleep

from part_five.zuoye1.page.main import Main


class TestAddMember:

    def setup(self):
        self.main = Main()

    def test_add_save_1(self):
        username = "aaa01"
        account = "aaa01"
        phone = "12312312311"
        page = self.main
        page.goto_add_member().add_member_save(username, account, phone)
        names = page.goto_contact().get_member()
        assert username in names

    def test_add_save_2(self):
        username = "aaa05"
        account = "aaa05"
        phone = "12312312315"
        page = self.main.goto_contact()
        page.goto_add_member().add_member_save(username, account, phone)
        names = page.get_member()
        assert username in names

    def test_add_cancel(self):
        username = "aaa02"
        account = "aaa02"
        phone = "12312312312"
        page = self.main
        page.goto_add_member().add_member_cancel(username, account, phone)
        names = page.goto_contact().get_member()
        assert username not in names

    def test_add_continue(self):
        username1 = "aaa03"
        account1 = "aaa03"
        phone1 = "12312312313"
        username2 = "aaa04"
        account2 = "aaa04"
        phone2 = "12312312314"
        page = self.main
        page1 = page.goto_add_member().add_member_continue(username1, account1, phone1)
        sleep(1)
        page1.add_member_save(username2, account2, phone2)
        names = page.goto_contact().get_member()
        assert (username1 in names and username2 in names)
