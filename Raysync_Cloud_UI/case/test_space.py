# coding=gbk
# 我的空间
import time
import pytest
import Base
import Handle
import logging
import os
from Base.Driver import Driver

class TestSpace:

    def setup_class(self):
        self.driver = Driver.get_driver()
        self.handle = Handle.HandleTotal(self.driver)

    def test_Download_folder(self):
        logging.info("-----------------test case Download folder start-----------------")
        self.handle.init_space.tap_Space()
        time.sleep(6)

        self.handle.init_space.tap_checkbox_all()
        logging.info("全选根目录下的所有文件（夹）")
        time.sleep(1)

        #单个文件夹
        # self.handle.init_space.tap_Download_Foloer()
        # logging.info("点击下载")
        # time.sleep(1)

        #单个文件
        self.handle.init_space.tap_Download_files()
        logging.info("点击下载")
        time.sleep(1)

        path = "E:\Python\Raysync_Cloud\Downlod\script/路径1.exe"
        # 运行指定路径下的文件
        os.startfile(path)
        time.sleep(8)

        self.handle.init_space.tap_checkbox_all()
        logging.info("取消全选根目录下的所有文件（夹）")
        time.sleep(1)

        # self.handle.init_space.tap_checkbox_first()
        # logging.info("取消勾选文件夹")
        # time.sleep(3)

    @pytest.mark.parametrize("info", Base.get_data("space", "Share Link"))
    def test_Share_Link(self,info):
        logging.info("-----------------test case Share_Link start-----------------")
        self.handle.init_space.tap_checkbox_first()
        logging.info("勾选根目录下的首个文件（夹）")
        time.sleep(1)

        self.handle.init_space.tap_Share_files()
        logging.info("点击文件分享按钮")
        time.sleep(1)

        self.handle.init_space.tap_Expiration_date()
        logging.info("开启链接过期时间")
        time.sleep(1)

        self.handle.init_space.tap_Share_Deadkube()
        logging.info("点击链接过期时间输入框")

        self.handle.init_space.input_Select_date(info["Date"])
        logging.info("链接过期年月日输入'{}'".format(info["Date"]))
        time.sleep(2)

        self.handle.init_space.tap_Select_time()
        logging.info("点击链接过期时间时分秒")
        time.sleep(1)

        self.handle.init_space.input_Select_time_clear()
        logging.info("清空链接过期时间时分秒")

        self.handle.init_space.input_Select_time(info["Time"])
        logging.info("链接过期时分秒输入'{}'".format(info["Time"]))
        time.sleep(1)

        self.handle.init_space.tap_Select_affirm()
        logging.info("点击链接过期时间确认按钮")
        time.sleep(1)

        self.handle.init_space.tap_Share_download()
        logging.info("点击链接过期下载次数按钮")
        time.sleep(1)

        self.handle.init_space.input_Share_num(info["Num"])
        logging.info("链接下载次数输入'{}'".format(info["Num"]))
        time.sleep(1)

        self.handle.init_space.tap_Share_login()
        logging.info("点击免登陆按钮")
        time.sleep(1)

        # self.driver.find_elements_by_class_name("el-switch__core")[3].click()
        # logging.info("开启邮件通知")
        # time.sleep(1)
        #
        # self.handle.init_space.tap_Email1_send()
        #
        # self.handle.init_space.input_Email2_send(info["E-mail"])
        # logging.info("分享链接邮件收件人输入'{}'".format(info["E-mail"]))
        # self.handle.init_space.tap_Email2_send()
        # time.sleep(1)
        #
        # self.handle.init_space.input_Email_text(info["Text"])
        # logging.info("分享链接邮件正文内容输入'{}'".format(info["Text"]))
        # time.sleep(2)
        #
        # down = self.driver.find_element_by_xpath("//*[@id='app']/section/main/section/section/div/div[2]/div/div/div[9]/div").text
        # logging.info("分享链接内容{}".format(down))
        # time.sleep(1)

        self.handle.init_space.tap_Share_affirm()
        logging.info("确认创建分享链接")
        time.sleep(2)

        msg = self.driver.find_element_by_xpath("//*[@id='app']/section/main/section/section/div/div/div/div/div[9]/div/div[2]/div[1]/div/div/span").text
        logging.info("Message提示‘{}’".format(msg))
        time.sleep(1)

        self.handle.init_space.tap_Share_close()
        logging.info("关闭邀请分享下载窗口")
        time.sleep(1)

        self.handle.init_space.tap_checkbox_first()
        logging.info("取消勾选文件夹")
        time.sleep(3)

    @pytest.mark.parametrize("info", Base.get_data("space", "New directory name"))
    def test_New_folder(self,info):

        logging.info("-----------------test case New folder start-----------------")
        self.handle.init_space.tap_New_Foloer()
        logging.info("点击新建文件夹按钮")
        time.sleep(1)

        self.handle.init_space.input_name(info["name"])
        logging.info("新建文件夹名称输入'{}'".format(info["name"]))
        time.sleep(1)

        self.handle.init_space.tap_New_affirm()
        logging.info("点击确定新建按钮")
        time.sleep(1)

        # 成功提示信息打印
        msg = self.driver.find_element_by_xpath("/html/body/div[2]/p").text
        logging.info("Message提示‘{}’".format(msg))
        time.sleep(1)

        # 执行异常创建文件夹
        # self.handle.init_space.tap_New_cancel()
        # logging.info("点击取消新建按钮")
        # time.sleep(2)

    @pytest.mark.parametrize("info", Base.get_data("space", "Search name"))
    def test_search_folder(self, info):
        time.sleep(2)
        logging.info("-----------------test case search folder start-----------------")
        self.handle.init_space.input_search(info["name"])
        logging.info("搜索文件名输入'{}'".format(info["name"]))
        self.handle.init_space.tap_search_ico()
        logging.info("点击搜索图标按钮")
        time.sleep(2)

        self.handle.init_space.input_search_clear()
        logging.info("清空搜索文件名输入框内容")
        self.driver.refresh()
        logging.info("刷新当前页面")
        time.sleep(3)

    # 重命名操作按钮暂无法定位，该测试用例不能执行
    # @pytest.mark.parametrize("info", Base.get_data("space", "Rename directory"))
    # def test_Rename_folder(self,info):
    #     logging.info("-----------------test case Rename folder start-----------------")
    #     self.handle.init_space.tap_Operation()
    #     logging.info("点击操作按钮")
    #     time.sleep(3)
    #
    #     self.handle.init_space.tap_Operation_rename()
    #     logging.info("点击重命名操作按钮")
    #     time.sleep(1)
    #
    #     self.handle.init_space.input_rename(info["name"])
    #     logging.info("重命名文件（夹）名称输入为'{}'".format(info["name"]))
    #     time.sleep(1)
    #
    #     self.handle.init_space.tap_Rename_affirm()
    #     logging.info("点击确定重命名按钮")
    #     time.sleep(3)

    @pytest.mark.parametrize("info", Base.get_data("space", "Invite_to_upload"))
    def test_Invite_to_upload(self,info):
        logging.info("-----------------test case Invite_to_upload start-----------------")
        self.handle.init_space.tap_checkbox_first()
        logging.info("勾选文件夹")
        time.sleep(1)

        self.handle.init_space.tap_Invite_to_upload()
        logging.info("点击邀请上传按钮")
        time.sleep(1)

        self.handle.init_space.tap_Expiration_date()
        logging.info("开启链接过期时间")
        time.sleep(1)

        self.handle.init_space.tap_Select_Deadkube()
        logging.info("点击链接过期时间输入框")
        self.handle.init_space.input_Select_date(info["Date"])
        logging.info("链接过期年月日输入'{}'".format(info["Date"]))
        time.sleep(2)

        self.handle.init_space.tap_Select_time()
        logging.info("点击链接过期时间时分秒")
        time.sleep(1)

        self.handle.init_space.input_Select_time_clear()
        logging.info("清空链接过期时间时分秒")

        self.handle.init_space.input_Select_time(info["Time"])
        logging.info("链接过期时分秒输入'{}'".format(info["Time"]))
        time.sleep(1)

        self.handle.init_space.tap_Select_affirm()
        logging.info("点击链接过期时间确认按钮")
        time.sleep(1)

    #     self.driver.find_elements_by_class_name("el-switch__core")[1].click()
    #     logging.info("开启邮件通知")
    #     time.sleep(1)
    #
    #     self.handle.init_space.tap_Email1_send()
    #     self.handle.init_space.input_Email2_send(info["E-mail"])
    #     logging.info("邀请链接邮件收件人输入'{}'".format(info["E-mail"]))
    #     self.handle.init_space.tap_Email2_send()
    #     time.sleep(1)
    #
    #     self.handle.init_space.input_Email_text(info["Text"])
    #     logging.info("邀请链接邮件正文内容输入'{}'".format(info["Text"]))
    #     time.sleep(1)
    #
    #     upload = self.driver.find_element_by_xpath("//*[@id='app']/section/main/section/section/div/div[2]/div/div/div[8]/div/div[2]").text
    #     logging.info("邀请链接内容{}".format(upload))

        self.handle.init_space.tap_upload_affirm()
        logging.info("确认创建邀请链接")
        time.sleep(1)

        msg = self.driver.find_element_by_xpath("//*[@id='app']/section/main/section/section/div/div/div/div/div[8]/div/div[2]/div[1]/div/div").text
        logging.info("Message提示‘{}’".format(msg))
        time.sleep(1)

        self.handle.init_space.tap_upload_close()
        logging.info("关闭邀请链接上传窗口")
        time.sleep(2)

    def test_Copy_folder(self):
        logging.info("-----------------test case Copy folder start-----------------")
        # self.handle.init_space.tap_checkbox_first()
        # logging.info("勾选文件夹")
        # time.sleep(1)

        self.handle.init_space.tap_Copy_Foloer()
        logging.info("点击复制按钮")
        time.sleep(2)

        self.handle.init_space.tap_Copy_space()
        logging.info("点击我的空间目录")
        time.sleep(1)

        self.handle.init_space.tap_Copy_catalogue()
        logging.info("点击我的空间根目录下的第二个子目录")
        time.sleep(1)

        self.handle.init_space.tap_Copy_affirm()
        logging.info("点击确认")
        time.sleep(1)

        msg = self.driver.find_element_by_xpath("/html/body/div[2]/p").text
        logging.info("Message提示‘{}’".format(msg))
        time.sleep(1)

    def test_Move_folder(self):
        logging.info("-----------------test case Move folder start-----------------")
        self.handle.init_space.tap_checkbox_first()
        logging.info("勾选文件夹")
        time.sleep(1)

        self.handle.init_space.tap_Move_Foloer()
        logging.info("点击移动")
        time.sleep(2)

        self.handle.init_space.tap_Move_space()
        logging.info("点击我的空间目录")
        time.sleep(1)

        self.handle.init_space.tap_Move_catalogue()
        logging.info("点击我的空间根目录下的第三个子目录")
        time.sleep(1)

        self.handle.init_space.tap_Move_affirm()
        logging.info("点击确认")
        time.sleep(3)

        msg = self.driver.find_element_by_xpath("/html/body/div[2]/p").text
        logging.info("Message提示‘{}’".format(msg))
        time.sleep(1)

    @pytest.mark.repeat(2)
    def test_Delete_folder(self):
        logging.info("-----------------test case Delete folder start-----------------")
        self.handle.init_space.tap_checkbox_first()
        logging.info("勾选文件（夹）")
        time.sleep(1)

        # self.handle.init_space.tap_checkbox_all()
        # logging.info("全选根目录下的所有文件（夹）")
        # time.sleep(1)

        self.handle.init_space.tap_Delete_Folder()
        logging.info("点击删除文件夹")
        time.sleep(1)

        # self.handle.init_space.tap_Delete_files()
        # logging.info("点击文件删除按钮")
        # time.sleep(1)

        # self.handle.init_space.tap_Delete_all()
        # logging.info("点击全选文件删除按钮")
        # time.sleep(1)

        self.handle.init_space.tap_Delete_affirm()
        logging.info("点击确定")
        time.sleep(3)

        msg = self.driver.find_element_by_xpath("/html/body/div[2]/p").text
        logging.info("Message提示‘{}’".format(msg))
        time.sleep(1)

if __name__ == '__main__':
    pytest.main(["-s", "test_space.py"])