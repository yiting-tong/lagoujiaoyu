from appium import webdriver

from part_six.zuoye1.pages.information_page import InformationPage


class App:
    def __init__(self):
        self.driver = None
        self.start()

    # 由于basepage基类会被调用多次，所以使用单独的app类来初始化driver
    def start(self):
        desire_cap = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            # 下次执行从当前页面开始，无需重新启动APP
            "noReset": "true",
            "dontStopAppOnReset": "true",
            # 使send keys可以输入中文
            "unicodeKeyBoard": "true",
            "resetKeyBoard": "true",
            "skipDeviceInitialization": "true"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(40)

    def goto_main(self):
        return InformationPage(self.driver)
