# coding=gbk
# 登录
import time
import pytest
from Base.Driver import Driver
import Base
import Handle
import logging
import os,sys
import allure


sys.path.append(os.getcwd())
url = "https://client.raysync.cloud/login?language=zh-CN"
class TestLogin:

    def setup_class(self):

        self.driver = Driver.get_driver()
        logging.info("启动谷歌浏览器")
        self.handle = Handle.HandleTotal(self.driver)
        self.driver.get(url)
        logging.info("浏览器访问'{}'网址".format(url))


    # def teardown_class(self):
    #     logging.info("------测试用例执行完毕，3s之后自动关闭浏览器------")
    #     time.sleep(3)
    #     Driver.quit_dirver()
    #     logging.info("成功关闭浏览器")

    @allure.feature("登录模块")
    # allure标题-title
    @allure.story("用例--登录测试")
    # allure描述信息
    @allure.description("该用例是针对登录的测试")
    @pytest.mark.parametrize("info", Base.get_data("login", "login_success"))
    def test_login(self,info):
        logging.info("-----------------test case login start-----------------")
        self.handle.init_login.input_num(info["num"])
        logging.info("镭速云传的账号输入为'{}'".format(info["num"]))

        self.handle.init_login.input_pwd(info["pwd"])
        logging.info("镭速云传的密码输入为'{}'".format(info["pwd"]))
        time.sleep(1)

        self.handle.init_login.tap_enter()
        logging.info("点击登录")
        time.sleep(3)


# 项目根目录执行生成报告
# 生成allure报告：allure generate report/xml -o report/html --clean

if __name__ == '__main__':
    pytest.main(["-s", "test_login.py"])