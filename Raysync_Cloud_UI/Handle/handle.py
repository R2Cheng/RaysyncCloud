# 这个模块负责管理Handle下的所有动作
import Handle
from selenium.webdriver.common.action_chains import ActionChains

class HandleTotal:

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)

    @property
    def init_login(self):
        return Handle.HandleLogin(self.driver)

    @property
    def init_space(self):
        return Handle.HandleSpace(self.driver)

    @property
    def init_register(self):
        return Handle.HandleRegister(self.driver)

    @property
    def init_account(self):
        return Handle.HandleAccount(self.driver)

    @property
    def init_sharing(self):
        return Handle.HandleSharing(self.driver)





