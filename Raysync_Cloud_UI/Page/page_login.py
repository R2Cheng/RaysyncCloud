# 登录页面
from selenium.webdriver.common.by import By
from Base.Action import BaseAction


class PageLogin(BaseAction):
    # 定位元素
    # 账号输入框
    num_feature = By.XPATH, "//*[@type = 'text']"
    # 密码输入框
    pwd_feature = By.XPATH,"//*[@id='app']/div/div/div/div[3]/div/div[1]/form/div[2]/div/div/input"
    # 登录按钮
    enter_feature = By.CLASS_NAME, "fill-button"

    # 1 账号输入框
    def get_num_ele(self):
        return self.get_element(self.num_feature)

    # 2 密码输入框
    def get_pwd_ele(self):
        return self.get_element(self.pwd_feature)

    # 3 提交登录按钮
    def get_enter_ele(self):
        return self.get_element(self.enter_feature)
