# coding=gbk
# 登出
import time
import pytest
import Base
import Handle
import logging
import os
from Base.Driver import Driver
from public.email import email
import allure


class TestLogout:

    def setup_class(self):
        self.driver = Driver.get_driver()
        self.handle = Handle.HandleTotal(self.driver)

    def teardown_class(self):
        logging.info("------结束测试用例------")
        time.sleep(3)
        Driver.quit_dirver()
        logging.info("关闭驱动")
        email()

    @allure.feature("登出模块")
    # allure标题-title
    @allure.story("用例--登出测试")
    # allure描述信息
    @allure.description("该用例是针对登出的测试")
    def test_logout(self):
        self.handle.init_space.tap_account_information()
        logging.info("点击账号信息下拉框")
        time.sleep(2)

        self.handle.init_space.tap_logout()
        logging.info("点击退出按钮")


if __name__ == '__main__':
    pytest.main(["-s", "test_logout.py"])
