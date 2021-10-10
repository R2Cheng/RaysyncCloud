import allure
from Page.page_account import PageAccount
from Base.Driver import Driver

class HandleAccount(PageAccount):

    # 1 点击账号中心
    @allure.step("点击账户中心")
    def tap_account(self):
        self.get_account_ele().click()

    # 2 点击更换手机
    @allure.step("点击更换手机")
    def tap_num(self):
        self.get_num_ele().click()

    # 3 输入手机号码
    @allure.step("输入手机号码")
    def input_phone(self, val):
        self.execute_input(self.get_phone_ele(), val)

    # 4 点击获取手机验证码按钮
    @allure.step("点击获取手机验证码")
    def tap_code(self):
        self.get_code_ele().click()

    # 5 点击确定更换手机按钮
    @allure.step("点击确定")
    def tap_enter(self):
        self.get_enter_ele().click()

    # 6 点击立即认证按钮
    @allure.step("点击立即认证")
    def tap_verify(self):
        self.get_verify_ele().click()

    # 7 点击完成认证按钮
    @allure.step("点击完成认证")
    def tap_verify_success(self):
        self.get_verify_success_ele().click()

    # 8 点击关闭按钮
    @allure.step("点击关闭")
    def tap_verify_close(self):
        self.get_verify_close_ele().click()

