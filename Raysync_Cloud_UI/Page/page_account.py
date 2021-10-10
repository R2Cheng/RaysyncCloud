# 账户中心页面
from selenium.webdriver.common.by import By
from Base.Action import BaseAction


class PageAccount(BaseAction):
    # 定位元素
    # 账号中心菜单
    account_feature = By.CLASS_NAME, "raysync-wodekongjian"

    # 更换手机按钮
    num_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div[2]/div/div[1]/div/div[2]/div[5]/div/button"
    # 手机号码输入框
    phone_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div[2]/div/div[7]/div/div[2]/form/div[1]/div/div/input"
    # 获取手机验证码按钮
    code_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div[2]/div/div[7]/div/div[2]/form/div[2]/div/div/div[2]/button"
    # 更换手机号码确认按钮
    enter_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div[2]/div/div[7]/div/div[2]/form/div[3]/div/button"

    # 立即认证按钮
    verify_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div[2]/div/div[1]/div/div[2]/div[1]/div/button"
    # 完成认证按钮
    verify_success_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div[2]/div/div[2]/div/div[2]/div[2]/button"
    # 关闭认证按钮
    verify_close_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div[3]/div/div[2]/div/button"

    # 1 账号中心菜单
    def get_account_ele(self):
        return self.get_element(self.account_feature)

    # 2 更换手机按钮
    def get_num_ele(self):
        return self.get_element(self.num_feature)

    # 3 手机号码输入框
    def get_phone_ele(self):
        return self.get_element(self.phone_feature)

    # 4 获取手机验证码按钮
    def get_code_ele(self):
        return self.get_element(self.code_feature)

    # 5 更换手机号码确认按钮
    def get_enter_ele(self):
        return self.get_element(self.enter_feature)

    # 6 立即认证按钮
    def get_verify_ele(self):
        return self.get_element(self.verify_feature)

    # 7 立即完成认证按钮
    def get_verify_success_ele(self):
        return self.get_element(self.verify_success_feature)

    # 8 关闭按钮
    def get_verify_close_ele(self):
        return self.get_element(self.verify_close_feature)



