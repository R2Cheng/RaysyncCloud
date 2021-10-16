# coding=gbk
# 注册
import time
import pytest
from Base.Driver import Driver
import Base
import Handle
import logging
from selenium.webdriver.common.action_chains import ActionChains
import random
import allure

url = "https://cloud-sit.raysync.cn/register"
class TestRegister:

    def setup_class(self):

        self.driver = Driver.get_driver()
        logging.info("启动谷歌浏览器")
        self.handle = Handle.HandleTotal(self.driver)
        self.driver.get(url)
        logging.info("浏览器访问'{}'网址".format(url))

    def teardown_class(self):
        logging.info("------测试用例执行完毕，3s之后自动关闭浏览器------")
        time.sleep(3)
        Driver.quit_dirver()
        logging.info("成功关闭浏览器")

    @allure.feature("注册模块")
    # allure标题-title
    @allure.story("用例--用户注册测试")
    # allure描述信息
    @allure.description("该用例是针对用户注册的测试")
    @pytest.mark.skip(reason="阿里云滑块不支持自动化打开的浏览器使用，该用例暂时跳过执行")
    @pytest.mark.parametrize("info", Base.get_data("register", "register_success"))
    def test_Register(self, info):
        logging.info("-----------------test case register start-----------------")
        self.handle.init_register.input_num(info["num"])
        logging.info("用户名输入为'{}'".format(info["num"]))

        self.handle.init_register.input_pwd(info["pwd"])
        logging.info("密码输入为'{}'".format(info["pwd"]))
        time.sleep(1)

        self.handle.init_register.input_tel(info["tel"])
        logging.info("手机号码输入为'{}'".format(info["tel"]))
        time.sleep(1)


        # 阿里云滑块无法使用脚本实现滑动操作，暂未找到解决办法
        div = self.driver.find_element_by_id("nc_2_n1z")
        ActionChains(self.driver).click_and_hold(on_element=div).perform()

        # 随机生成移动距离数值
        x1 = random.randrange(20, 200)

        ActionChains(self.driver).move_to_element_with_offset(to_element=div, xoffset=x1, yoffset=50).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element_with_offset(to_element=div, xoffset=x1, yoffset=50).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element_with_offset(to_element=div, xoffset=x1, yoffset=50).release().perform()
        logging.info("滑动滑块")
        time.sleep(3)


if __name__ == '__main__':
    pytest.main(["-s", "test_register.py"])