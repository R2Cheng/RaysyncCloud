# coding=gbk
# 账户中心
import time
import pytest
from Base.Driver import Driver
import Base
import Handle
import logging
import os,sys
import allure



sys.path.append(os.getcwd())


class TestAccount:

    def setup_class(self):
        self.driver = Driver.get_driver()
        self.handle = Handle.HandleTotal(self.driver)

    @allure.feature("账户中心模块")
    # allure标题-title
    @allure.story("用例--更换手机号码测试")
    # allure描述信息
    @allure.description("该用例是针对更换手机号码的测试")
    @pytest.mark.skip(reason="需要修改更换手机的data数值，该用例暂时跳过执行")
    @pytest.mark.parametrize("info", Base.get_data("account", "Phone_success"))
    def test_phone(self,info):
        logging.info("-----------------test case phone start-----------------")

        self.handle.init_account.tap_account()
        logging.info("点击账号中心")
        time.sleep(1)

        self.handle.init_account.tap_num()
        logging.info("点击更换手机")
        time.sleep(1)

        self.handle.init_account.input_phone(info["num"])
        logging.info("更换手机号码为'{}'".format(info["num"]))
        time.sleep(1)

        self.handle.init_account.tap_code()
        logging.info("点击获取手机验证码")
        time.sleep(1)

        msg = self.driver.find_element_by_xpath("/html/body/div[3]/p").text
        logging.info("Message提示‘{}’".format(msg))
        time.sleep(12)

        self.handle.init_account.tap_enter()
        logging.info("点击确定")
        time.sleep(5)

    @allure.feature("账户中心模块")
    # allure标题-title
    @allure.story("用例--账号验证测试")
    # allure描述信息
    @allure.description("该用例是针对已绑定邮箱或手机号账号的验证测试")
    @pytest.mark.skip(reason="需要登录未认证过得账号，该用例暂时跳过执行")
    def test_verify(self):
        logging.info("-----------------test case verify start-----------------")

        self.handle.init_account.tap_verify()
        logging.info("点击确定")
        time.sleep(15)

        self.handle.init_account.tap_verify_success()
        logging.info("点击完成认证")
        time.sleep(1)

        # msg = self.driver.find_element_by_xpath("/html/body/div[3]/p").text
        # logging.info("Message提示‘{}’".format(msg))
        # time.sleep(1)

        self.handle.init_account.tap_verify_close()
        logging.info("点击关闭")
        time.sleep(1)

if __name__ == '__main__':
    pytest.main(["-s", "test_account.py"])