# 我的分享
import allure
from Page.page_sharing import PageSharing
from Base.Driver import Driver

class HandleSharing(PageSharing):

    # 1 点击我的分享菜单
    def tap_sharing(self):
        self.get_sharing_ele().click()

    # 2 勾选分享下载链接
    @allure.step("勾选分享下载链接")
    def tap_first_sharing(self):
        self.get_first_sharing_ele().click()

    # 3 点击编辑按钮
    @allure.step("点击编辑按钮")
    def tap_Edit(self):
        self.get_Edit_ele().click()

    # 4 点击下载次数按钮
    @allure.step("点击下载限制次数按钮")
    def tap_download(self):
        self.get_download_ele().click()

    # 5 输入下载限制次数
    @allure.step("输入下载限制次数")
    def input_download_times(self, val):
        self.execute_input(self.get_download_times_ele(),val)

    # 6 点击免登录按钮
    @allure.step("点击免登录")
    def tap_without_login(self):
        self.get_without_login_ele().click()

    # 7 点击确定按钮
    @allure.step("点击确定")
    def tap_confirm(self):
        self.get_confirm_ele().click()

    # 8 点击邀请上传
    @allure.step("点击邀请上传")
    def tap_upload(self):
        self.get_upload_ele().click()

    # 9 勾选第一个邀请上传连接
    @allure.step("勾选第一个邀请上传连接")
    def tap_first_upload(self):
        self.get_first_upload_ele().click()

    # 10 点击复制链接按钮

    @allure.step("点击复制链接")
    def tap_copy_link(self):
        self.get_copy_link_ele().click()

    # 11 点击取消分享按钮
    @allure.step("点击取消分享")
    def tap_cancel_sharing(self):
        self.get_cancel_sharing_ele().click()

    # 12 点击取消分享确认按钮
    @allure.step("点击确定")
    def tap_cancel_confirm(self):
        self.get_cancel_confirm_ele().click()


