import allure
from Page.page_login import PageLogin
from Base.Driver import Driver

class HandleLogin(PageLogin):

    # 1 输入账号
    @allure.step("输入账号")
    def input_num(self,val):
        self.execute_input(self.get_num_ele(),val)

    # 2 输入密码
    @allure.step("输入密码")
    def input_pwd(self,val):
        self.execute_input(self.get_pwd_ele(),val)

    # 3 点击登录
    @allure.step("点击登录")
    def tap_enter(self):
        self.get_enter_ele().click()
