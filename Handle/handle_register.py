import allure
from Page.page_register import PageRegister

class HandleRegister(PageRegister):

    # 1 输入账号
    @allure.step("输入账号")
    def input_num(self, val):
        self.execute_input(self.get_num_ele(), val)

    # 2 输入密码
    @allure.step("输入密码")
    def input_pwd(self,val):
        self.execute_input(self.get_pwd_ele(),val)

    # 2 输入手机号码
    @allure.step("输入手机号码")
    def input_tel(self, val):
        self.execute_input(self.get_tel_ele(), val)

    # 3 点击下一步
    #@allure.step("点击下一步")
    # def tap_enter(self):
    #     self.get_enter_ele().click()
