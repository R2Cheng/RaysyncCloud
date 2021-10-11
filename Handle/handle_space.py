import allure
from Page.page_space import PageSpace
from selenium.webdriver.common.keys import Keys

class HandleSpace(PageSpace):

    # 点击我的空间
    @allure.step("点击菜单栏-我的空间")
    def tap_Space(self):
        self.get_Space_ele().click()

    # 1 新建文件夹
    # 1.1 点击新建文件夹
    @allure.step("点击新建文件夹")
    def tap_New_Foloer(self):
        self.get_New_Foloer_ele().click()

    # 1.2 输入新文件夹名称
    @allure.step("输入新文件夹名称")
    def input_name(self, val):
        self.execute_input(self.get_Adirectory_name_ele(), val)

    # 1.3 点击‘确定’
    @allure.step("点击确定")
    def tap_New_affirm(self):
        self.get_New_affirm_ele().click()

    # 1.4 点击“取消”
    @allure.step("点击取消")
    def tap_New_cancel(self):
        self.get_New_cancel_ele().click()

    # 2 重命名文件（夹）
    @allure.step("点击文件（夹）操作")
    def tap_Operation(self):
        self.get_Operation_ele().click()

    # 2.1 点击重命名操作按钮
    @allure.step("点击重命名")
    def tap_Operation_rename(self):
        self.get_Operation_rename_ele().click()

    # 2.2 输入重命名文件目录名称
    @allure.step("输入新的文件（夹）名称")
    def input_rename(self, val):
        self.execute_input(self.get_Rename_ele(), val)

    # 2.3 点击确认重命名按钮
    @allure.step("点击确定")
    def tap_Rename_affirm(self):
        self.get_Rename_affirm_ele().click()

    # 3 搜索文件(夹)
    # 3.1 输入搜索文件（夹）名称
    @allure.step("输入搜索文件（夹）名称")
    def input_search(self, val):
        self.execute_input(self.get_search_ele(), val)

    # 3.2 点击搜索图标ico
    @allure.step("点击搜索图标")
    def tap_search_ico(self):
        self.get_search_ico_ele().click()

    # 3.3 清空搜索内容
    @allure.step("清空搜索内容")
    def input_search_clear(self):
        self.get_search_ele().clear()

    # 4 删除文件夹
    # 4.1 勾选首个文件（夹）
    @allure.step("勾选首个文件（夹）")
    def tap_checkbox_first(self):
        self.get_checkbox_first_ele().click()

    # 4.2 全选文件
    @allure.step("全选文件（夹）")
    def tap_checkbox_all(self):
        self.get_checkbox_all_ele().click()

    # 4.3 点击文件夹删除按钮
    @allure.step("点击删除")
    def tap_Delete_Folder(self):
        self.get_Delete_Foloe_ele().click()

    # 4.4 点击文件删除按钮
    @allure.step("点击删除")
    def tap_Delete_files(self):
        self.get_Delete_files_ele().click()

    # 4.5 点击全选文件删除按钮
    @allure.step("点击删除")
    def tap_Delete_all(self):
        self.get_Delete_all_ele().click()

    # 4.6 确认删除
    @allure.step("点击确认")
    def tap_Delete_affirm(self):
        self.get_Delete_affirm_ele().click()



    # 5 创建邀请上传连接
    # 5.1 点击邀请上传连接按钮
    @allure.step("点击邀请上传")
    def tap_Invite_to_upload(self):
        self.get_Invite_to_upload_ele().click()

    # 5.2 点击链接过期设置
    @allure.step("点击链接过期开关")
    def tap_Expiration_date(self):
        self.get_Expiration_date_ele().click()

    # 5.3 点击设置过期时间
    @allure.step("点击过期时间")
    def tap_Select_Deadkube(self):
        self.get_Select_Deadkube_ele().click()

    # 5.4 输入过期时间（年月日）
    @allure.step("输入过期时间-年月日")
    def input_Select_date(self, val):
        self.execute_input(self.get_Select_date_ele(), val)

    # 5.5 输入过期时间（时分秒）
    @allure.step("输入过期时间-时分秒")
    def input_Select_time(self, val):
        self.execute_input(self.get_Select_time_ele(), val)

    # 5.5.1清空过期时间（时分秒）内容
    @allure.step("清空过期时间-时分秒内容")
    def input_Select_time_clear(self):
        self.get_Select_time_ele().clear()

    # 5.5.2点击过期时间时分秒输入框
    @allure.step("点击过期时间-年月日输入框")
    def tap_Select_time(self):
        self.get_Select_time_ele().click()

    # 5.6 确定设置过期时间按钮
    @allure.step("点击确定")
    def tap_Select_affirm(self):
        self.get_Select_affirm_ele().click()

    # 5.7 点击设置邮件通知
    @allure.step("点击邮件通知开关")
    def tap_Email_notification(self):
        self.get_Email_notification_ele().click()

    # 5.7 点击设置邮件通知收件人
    @allure.step("点击邮件通知收件人")
    def tap_Email1_send(self):
        self.get_Email1_send_ele().click()

    # 输入邮件收件人内容
    @allure.step("输入邮件通知收件人")
    def input_Email2_send(self, val):
        self.execute_input(self.get_Email2_send_ele(), val)

    # 键盘回车
    @allure.step("按键盘回车键")
    def tap_Email2_send(self):
        self.get_Email2_send_ele().send_keys(Keys.ENTER)

    # 5.8 点击设置邮件通知收件内容
    @allure.step("点击邮件通知正文内容")
    def input_Email_text(self, val):
        self.execute_input(self.get_Email_text_ele(), val)

    # 5.9 邀请上传链接确认创建
    @allure.step("点击创建连接")
    def tap_upload_affirm(self):
        self.get_upload_affirm_ele().click()

    # 5.10 关闭邀请上传窗口
    @allure.step("点击关闭")
    def tap_upload_close(self):
        self.get_upload_close_ele().click()

    # 5.11 复制邀请上传链接和密码
    @allure.step("点击复制链接和密码")
    def tap_upload_Copy(self):
        self.get_upload_Copy_ele().click()


    # 6 创建分享下载链接
    # 6.1 点击分享下载链接按钮（文件夹）
    @allure.step("点击分享")
    def tap_Share_Foloer(self):
        self.get_Share_Foloer_ele().click()

    # 6.2 点击分享下载链接按钮（文件）
    @allure.step("点击分享")
    def tap_Share_files(self):
        self.get_Share_files_ele().click()

    # 6.3 点击设置过期时间
    @allure.step("点击过期时间开关")
    def tap_Share_Deadkube(self):
        self.get_Share_Deadkube_ele().click()

    # 6.4 点击分享下载次数按钮
    @allure.step("点击下载次数限制开关")
    def tap_Share_download(self):
        self.get_Share_download_ele().click()

    # 6.5 输入分享下载次数
    @allure.step("输入下载限制次数")
    def input_Share_num(self, val):
        self.execute_input(self.get_Share_num_ele(), val)

    # 6.6 点击免登陆按钮
    @allure.step("点击免登陆开关")
    def tap_Share_login(self):
        self.get_Share_login_ele().click()

    # 6.7 点击设置分享下载邮件通知按钮
    @allure.step("点击邮件通知开关")
    def tap_Share_notification(self):
        self.get_Share_notification_ele().click()

    # 6.8 点击分享下载链接确认创建按钮
    @allure.step("点击创建链接")
    def tap_Share_affirm(self):
        self.get_Share_affirm_ele().click()

    # 6.9 点击关闭分享下载窗口
    @allure.step("点击关闭")
    def tap_Share_close(self):
        self.get_Share_close_ele().click()

    # 6.10 点击复制分享下载链接和密码按钮
    @allure.step("点击复制链接和密码")
    def tap_Share_Copy(self):
        self.get_Share_Copy_ele().click()

    # 7 复制文件（夹）
    # 7.1 复制文件
    @allure.step("点击复制")
    def tap_Copy_files(self):
        self.get_Copy_files_ele().click()

    # 7.2 复制文件夹
    @allure.step("点击复制")
    def tap_Copy_Foloer(self):
        self.get_Copy_Foloer_ele().click()

    # 7.1 点击复制文件（窗口）-我的空间
    @allure.step("点击我的空间")
    def tap_Copy_space(self):
        self.get_Copy_space_ele().click()

    # 7.1 点击复制文件（窗口）-我的空间第二个目录
    @allure.step("点击我的空间根目下的第二个子目录")
    def tap_Copy_catalogue(self):
        self.get_Copy_catalogue_ele().click()

    # 7.1 点击确认复制文件（夹）按钮
    @allure.step("点击确认")
    def tap_Copy_affirm(self):
        self.get_Copy_affirm_ele().click()

    # 8 退出登录
    # 8.1 点击用户账号下拉框
    @allure.step("点击下拉框")
    def tap_account_information(self):
        self.get_account_information_ele().click()

    # 8.2 点击退出
    @allure.step("点击退出")
    def tap_logout(self):
        self.get_logout_ele().click()

    # 9 文件移动
    # 9.1 点击移动文件夹按钮
    @allure.step("点击移动")
    def tap_Move_Foloer(self):
        self.get_Move_Foloer_ele().click()

    # 9.2 点击移动文件按钮
    @allure.step("点击移动")
    def tap_Move_files(self):
        self.get_Move_Foloer_ele().click()

    # 9.3 点击移动多个文件或者多个文件夹按钮
    @allure.step("点击移动")
    def tap_Move_plural(self):
        self.get_Move_plural_ele().click()

    # 9.4 点击移动窗口-我的空间
    @allure.step("点击我的空间")
    def tap_Move_space(self):
        self.get_Move_space_ele().click()

    # 9.5 点击移动窗口-我的空间第二个目录
    @allure.step("点击我的空间下第三个目录")
    def tap_Move_catalogue(self):
        self.get_Move_catalogue_ele().click()

    # 9.6 点击移动窗口-确认按钮
    @allure.step("点击移动")
    def tap_Move_affirm(self):
        self.get_Move_affirm_ele().click()


    # 10 文件下载
    @allure.step("点击下载")
    def tap_Download_Foloer(self):
        self.get_Download_Foloer_ele().click()

    # 10.1 文件夹下载
    @allure.step("点击下载")
    def tap_Download_files(self):
        self.get_Download_files_ele().click()