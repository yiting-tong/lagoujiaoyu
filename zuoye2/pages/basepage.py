import json
from typing import List, Dict

import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    _blacklist = [(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/h86']")]
    _max_num = 5
    _error_num = 0
    _params = {}

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_click(self, locator):
        try:
            element = self.driver.find_element_by_xpath(locator)
            element.click()
            self._error_num = 0
        except Exception as e:
            if self._error_num > self._max_num:
                self._error_num = 0
                raise e
            self._error_num += 1
            for black in self._blacklist:
                elements = self.driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return self.find_click(locator)
            raise e

    def find_send_keys(self, locator, content):
        self.driver.find_element_by_xpath(locator).send_keys(content)

    # 滑动查找点击
    def swip_click(self, text):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{text}").instance(0));').click()

    def parse_action(self, path, fun_name):
        with open(path, "r", encoding="utf-8") as f:
            function1 = yaml.safe_load(f)
        steps: List[Dict] = function1[fun_name]
        raw = json.dumps(steps)
        for key, value in self._params.items():
            raw = raw.replace("${" + key + "}", value)
        steps = json.loads(raw)
        for step in steps:
            if step["action"] == "find_click":
                self.find_click(step["locator"])
            elif step["action"] == "find_send_keys":
                self.driver.find_element_by_xpath(step["locator"]).send_keys(step["content"])
            elif step["action"] == "swip_click":
                self.swip_click(step["locator"])
