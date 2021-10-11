from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    # 1 工具方page_login.py法之定位元素
    def get_element(self, feature):
        """
        可以定位目标元素
        :param feature: 元组， 表示目标元素信息特征
        :return: obj ，如果存则是元素对象，如果不存在则是None
        """
        wait = WebDriverWait(self.driver, 5, 1)
        try:
            obj = wait.until(lambda x: x.find_element(*feature))
        except Exception as e:
            # 说明此时目标元素存在，返回None
            return None
        else:
            # 说明此时找到了目标元素
            return obj

    def get_elements(self, feature):
        """
        可以定位目标元素
        :param feature: 元组， 表示目标元素信息特征
        :return: obj ，如果存则是元素对象，如果不存在则是None
        """
        wait = WebDriverWait(self.driver, 5, 1)
        try:
            obj = wait.until(lambda x: x.find_elements(*feature))
        except Exception as e:
            # 说明此时目标元素存在，返回None
            return None
        else:
            # 说明此时找到了目标元素
            return obj

    # 2 工具方法之输入
    def execute_input(self, feature, val):

        # 判断用户传入的是否为元组
        if isinstance(feature, tuple):
            # 说明用户传的是元组，此时就应该先找再输入
            feature = self.get_element(feature)

        # 无论传的是什么，我们都要执行输入操作
        feature.send_keys(val)

    # 3 工具方法之点击
    def execute_tap(self, feature):
        action = TouchAction(self.driver)

        # 判断用户给的是什么
        if isinstance(feature, tuple):
            # 此时说明用户组的是元组，那么就先找后点击
            feature = self.get_element(feature)

        action.tap(feature)
        action.perform()

    # 4 工具方法之获取设备尺寸
    def get_size(self):
        return self.driver.get_window_size()

    # 5 工具方法之向左滑屏
    def swipe_left(self):
        win_size = self.get_size()
        w = win_size["width"]
        h = win_size["height"]
        self.driver.swipe(w * 0.9, h * 0.5, w * 0.1, h * 0.5)

    # 6 工具方法之向上滑屏
    def swipe_top(self, time=1500):
        win_size = self.get_size()
        w = win_size["width"]
        h = win_size["height"]
        self.driver.swipe(w * 0.5, h * 0.9, w * 0.5, h * 0.1, time)

    # 7 工具方法之递归找元素
    def get_ele_recursion(self, feature):
        obj = self.get_element(feature)
        if obj:
            # 此时说明元素被找到了
            return obj
        else:
            # 没找到则滑屏，然后继续查找
            self.swipe_top(time=3200)
            return self.get_ele_recursion(feature)

