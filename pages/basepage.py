from typing import List, Dict

import yaml
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_click(self, locator):
        self.driver.find_element_by_xpath(locator).click()

    def find_send_keys(self, locator, content):
        self.driver.find_element_by_xpath(locator).send_keys(content)

    def parse_action(self, path):
        with open(path, "r", encoding="utf-8") as f:
            steps: List[Dict] = yaml.safe_load(f)
        for step in steps:
            if step["action"] == "find_click":
                self.find_click(step["locator"])
            elif step["action"] == "find_send_keys":
                self.driver.find_element_by_xpath(step["locator"]).send_keys(step["content"])
