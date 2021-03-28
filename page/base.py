# base基类
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    _base_url = ""

    # 初始化webdriver
    def __init__(self, driver: WebDriver = None):
        if driver is None:
            self._driver = webdriver.Chrome()
        else:
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)

        self._driver.maximize_window()
        self._driver.implicitly_wait(5)

    # 封装find element方法
    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    # 封装find elements方法
    def finds(self, by, locator):
        return self._driver.find_elements(by, locator)

    # 封装显示等待
    def wait(self, timeout, locator):
        return WebDriverWait(self._driver, timeout).until(expected_conditions.element_to_be_clickable(locator))
