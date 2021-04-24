from part_six.zuoye2.pages.basepage import BasePage
from part_six.zuoye2.pages.contact_index_page import ContactIndex


class SearchMember(BasePage):
    def search_member(self, name):
        self._params["name"] = name
        self.parse_action("../pages/search_member.yaml", "search_member")
        return self

    def choose_member(self, department):
        self._params["department"] = department
        self.parse_action("../pages/search_member.yaml", "choose_member")
        return ContactIndex(self.driver)

    def verify_delete(self):
        self.driver.find_element_by_xpath("//*[@text='无搜索结果']")
