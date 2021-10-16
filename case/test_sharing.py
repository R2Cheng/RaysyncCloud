# coding=gbk
# 我的分享
import time
import pytest
from Base.Driver import Driver
import Base
import Handle
import logging
import allure
class TestSharing:

    def setup_class(self):

        self.driver = Driver.get_driver()
        self.handle = Handle.HandleTotal(self.driver)


    @allure.feature("我的分享模块")
    # allure标题-title
    @allure.story("用例--编辑分享下载链接测试")
    # allure描述信息
    @allure.description("该用例是针对编辑分享下载链接的测试")
    def test_sharing(self):
        logging.info("-----------------test case sharing start-----------------")

        self.handle.init_sharing.tap_sharing()
        logging.info("点击菜单我的分享")
        time.sleep(1)

        self.handle.init_sharing.tap_first_sharing()
        logging.info("勾选分享下载链接")
        time.sleep(2)

        self.handle.init_sharing.tap_Edit()
        logging.info("点击编辑")
        time.sleep(1)

        self.handle.init_sharing.tap_download()
        logging.info("点击下载限制次数")
        time.sleep(1)

        self.handle.init_sharing.tap_without_login()
        logging.info("点击免登陆")
        time.sleep(1)

        element = self.driver.find_element_by_xpath("//*[@id='app']/section/main/section/section/div/div/div/div[3]/div/div[2]").text
        logging.info("分享链接内容{}".format(element))

        self.handle.init_sharing.tap_confirm()
        logging.info("点击确定")
        time.sleep(1)

        msg = self.driver.find_element_by_class_name("el-message__content").text
        logging.info("Message提示‘{}’".format(msg))
        time.sleep(2)

        self.handle.init_sharing.tap_first_sharing()
        logging.info("勾选分享下载链接")
        time.sleep(2)

        self.handle.init_sharing.tap_copy_link()
        logging.info("点击复制链接")
        time.sleep(1)

        msg = self.driver.find_element_by_class_name("el-message__content").text
        logging.info("Message提示‘{}’".format(msg))
        time.sleep(2)

        self.handle.init_sharing.tap_cancel_sharing()
        logging.info("点击取消分享")
        time.sleep(1)

        self.handle.init_sharing.tap_cancel_confirm()
        logging.info("点击确定")
        time.sleep(3)

        msg = self.driver.find_element_by_class_name("el-message__content").text
        logging.info("Message提示‘{}’".format(msg))
        time.sleep(1)

    @allure.feature("我的分享模块")
    # allure标题-title
    @allure.story("用例--编辑邀请上传链接测试")
    # allure描述信息
    @allure.description("该用例是针对编辑邀请上传链接的测试")
    def test_upload(self):
        logging.info("-----------------test case upload start-----------------")
        self.handle.init_sharing.tap_upload()
        logging.info("点击邀请上传")
        time.sleep(1)

        self.handle.init_sharing.tap_first_upload()
        logging.info("勾选邀请上传链接")
        time.sleep(1)

        self.handle.init_sharing.tap_copy_link()
        logging.info("点击复制链接")
        time.sleep(1)

        msg = self.driver.find_element_by_class_name("el-message__content").text
        logging.info("Message提示‘{}’".format(msg))
        time.sleep(2)

        self.handle.init_sharing.tap_cancel_sharing()
        logging.info("点击取消分享")
        time.sleep(1)

        self.handle.init_sharing.tap_cancel_confirm()
        logging.info("点击确定")
        time.sleep(3)

        logging.info("Message提示‘{}’".format(msg))
        time.sleep(2)


if __name__ == '__main__':
    pytest.main(["-s", "test_sharing.py"])