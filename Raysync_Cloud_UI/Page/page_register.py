# 登录页面
from selenium.webdriver.common.by import By
from Base.Action import BaseAction


class PageRegister(BaseAction):
    # 定位元素
    num_feature = By.XPATH, "//*[@id='app']/div/div[1]/div/form/div[2]/div/div/input"
    pwd_feature = By.XPATH, "//*[@id='app']/div/div[1]/div/form/div[3]/div/div/input"
    tel_feature = By.XPATH, "//*[@id='app']/div/div[1]/div/form/div[4]/div/div/input"
    sliding1_feature = By.CLASS_NAME, "btn_slide"
    sliding2_feature = By.CLASS_NAME, "btn_ok"
    enter_feature = By.ID, "2register"

    # 1 账号输入框
    def get_num_ele(self):
        return self.get_element(self.num_feature)

    # 2 密码输入框
    def get_pwd_ele(self):
        return self.get_element(self.pwd_feature)

    # 3 手机号码输入框
    def get_tel_ele(self):
        return self.get_element(self.tel_feature)

    # 4 原滑块
    def get_sliding1_ele(self):
        return self.get_element(self.sliding1_feature)

    # 4.1 目标滑块
    def get_sliding2_ele(self):
        return self.get_element(self.sliding2_feature)

    # 5 提交注册按钮
    def get_enter_ele(self):
        return self.get_element(self.enter_feature)
