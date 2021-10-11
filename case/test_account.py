# coding=gbk
# 账户中心
import time
import pytest
from Base.Driver import Driver
import Base
import Handle
import logging
import os,sys
sys.path.append(os.getcwd())


class TestAccount:

    def setup_class(self):
        self.driver = Driver.get_driver()
        self.handle = Handle.HandleTotal(self.driver)

    # @pytest.mark.parametrize("info", Base.get_data("account", "Phone_success"))
    # def test_phone(self,info):
    #     logging.info("-----------------test case phone start-----------------")
    #
    #     self.handle.init_account.tap_account()
    #     logging.info("点击账号中心")
    #     time.sleep(1)
    #
    #     self.handle.init_account.tap_num()
    #     logging.info("点击更换手机")
    #     time.sleep(1)
    #
    #     self.handle.init_account.input_phone(info["num"])
    #     logging.info("更换手机号码为'{}'".format(info["num"]))
    #     time.sleep(1)
    #
    #     self.handle.init_account.tap_code()
    #     logging.info("点击获取手机验证码")
    #     time.sleep(1)
    #
    #     msg = self.driver.find_element_by_xpath("/html/body/div[3]/p").text
    #     logging.info("Message提示‘{}’".format(msg))
    #     time.sleep(12)
    #
    #     self.handle.init_account.tap_enter()
    #     logging.info("点击确定")
    #     time.sleep(5)

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