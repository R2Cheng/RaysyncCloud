# coding=gbk
# �˻�����
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

    @allure.feature("�˻�����ģ��")
    # allure����-title
    @allure.story("����--�����ֻ��������")
    # allure������Ϣ
    @allure.description("����������Ը����ֻ�����Ĳ���")
    @pytest.mark.skip(reason="��Ҫ�޸ĸ����ֻ���data��ֵ����������ʱ����ִ��")
    @pytest.mark.parametrize("info", Base.get_data("account", "Phone_success"))
    def test_phone(self,info):
        logging.info("-----------------test case phone start-----------------")

        self.handle.init_account.tap_account()
        logging.info("����˺�����")
        time.sleep(1)

        self.handle.init_account.tap_num()
        logging.info("��������ֻ�")
        time.sleep(1)

        self.handle.init_account.input_phone(info["num"])
        logging.info("�����ֻ�����Ϊ'{}'".format(info["num"]))
        time.sleep(1)

        self.handle.init_account.tap_code()
        logging.info("�����ȡ�ֻ���֤��")
        time.sleep(1)

        msg = self.driver.find_element_by_xpath("/html/body/div[3]/p").text
        logging.info("Message��ʾ��{}��".format(msg))
        time.sleep(12)

        self.handle.init_account.tap_enter()
        logging.info("���ȷ��")
        time.sleep(5)

    @allure.feature("�˻�����ģ��")
    # allure����-title
    @allure.story("����--�˺���֤����")
    # allure������Ϣ
    @allure.description("������������Ѱ�������ֻ����˺ŵ���֤����")
    @pytest.mark.skip(reason="��Ҫ��¼δ��֤�����˺ţ���������ʱ����ִ��")
    def test_verify(self):
        logging.info("-----------------test case verify start-----------------")

        self.handle.init_account.tap_verify()
        logging.info("���ȷ��")
        time.sleep(15)

        self.handle.init_account.tap_verify_success()
        logging.info("��������֤")
        time.sleep(1)

        # msg = self.driver.find_element_by_xpath("/html/body/div[3]/p").text
        # logging.info("Message��ʾ��{}��".format(msg))
        # time.sleep(1)

        self.handle.init_account.tap_verify_close()
        logging.info("����ر�")
        time.sleep(1)

if __name__ == '__main__':
    pytest.main(["-s", "test_account.py"])