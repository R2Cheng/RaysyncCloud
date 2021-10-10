# 我的分享
from selenium.webdriver.common.by import By
from Base.Action import BaseAction


class PageSharing(BaseAction):
    # 定位元素
    # 菜单-我的分享
    sharing_feature = By.XPATH, "//*[@id='app']/section/main/section/aside/ul/div[2]/li/i"
    # 第一个分享下载链接
    first_sharing_feature = By.XPATH, "//*[@id='pane-share']/div[1]/div[3]/table/tbody/tr/td[1]/div/label/span/span"
    # 编辑按钮
    Edit_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div[1]/div[2]/button[1]"
    # 下载次数按钮
    download_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div[3]/div/div[2]/div/div[1]/div/span[2]"
    # 下载次数输入框
    download_times_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div[2]/div/div[3]/div/div[2]/div/div[2]/div/input"
    # 免登陆按钮
    without_login_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div[3]/div/div[2]/div/p[7]/div/span[2]"
    # 确定按钮
    confirm_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div[3]/div/div[3]/span/button[1]"

    # 邀请上传
    upload_feature = By.ID, "tab-invite"
    # 勾选第一个邀请上传连接
    first_upload_feature = By.XPATH, "//*[@id='pane-invite']/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span"
    # 复制按钮
    copy_link_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div[1]/div[2]/button[2]"
    # 取消分享按钮
    cancel_sharing_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div[1]/div[2]/button[3]"
    # 取消分享确认按钮
    cancel_confirm_feature = By.XPATH, "/html/body/div[2]/div/div[3]/button[2]"





    # 1 菜单-我的分享
    def get_sharing_ele(self):
        return self.get_element(self.sharing_feature)

    # 2 第一个分享下载链接
    def get_first_sharing_ele(self):
        return self.get_element(self.first_sharing_feature)

    # 3 编辑按钮
    def get_Edit_ele(self):
        return self.get_element(self.Edit_feature)

    # 4 下载次数按钮
    def get_download_ele(self):
        return self.get_element(self.download_feature)

    # 5 下载次数输入框
    def get_download_times_ele(self):
        return self.get_element(self.download_times_feature)

    # 6 免登陆按钮
    def get_without_login_ele(self):
        return self.get_element(self.without_login_feature)

    # 7 确定按钮
    def get_confirm_ele(self):
        return self.get_element(self.confirm_feature)


    # 8 邀请上传
    def get_upload_ele(self):
        return self.get_element(self.upload_feature)

    # 9 勾选第一个邀请上传连接
    def get_first_upload_ele(self):
        return self.get_element(self.first_upload_feature)

    # 10 复制链接按钮
    def get_copy_link_ele(self):
        return self.get_element(self.copy_link_feature)

    # 11 取消分享按钮
    def get_cancel_sharing_ele(self):
        return self.get_element(self.cancel_sharing_feature)

    # 12 取消分享确认按钮
    def get_cancel_confirm_ele(self):
        return self.get_element(self.cancel_confirm_feature)

