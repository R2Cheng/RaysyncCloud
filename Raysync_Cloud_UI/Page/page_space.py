# 我的空间页面
from selenium.webdriver.common.by import By
from Base.Action import BaseAction


class PageSpace(BaseAction):

    # 定位元素
    # 我的空间
    Space_feature = By.CLASS_NAME, "raysync-kongjian"
    # 上传按钮
    Upload_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div/div[1]/div[1]/div/button"
    # 上传文件按钮
    Upload_files_feature = By.XPATH, "//*[@id='dropdown-menu-1754']/li[1]"
    # 上传文件夹按钮
    Upload_folders_feature = By.XPATH, "//*[@id='dropdown-menu-1754']/li[2]"

    # 新建文件夹按钮
    New_Foloer_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div/div[1]/div[1]/button"
    # 新建文件夹目录名称输入框
    Adirectory_name_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div/div[3]/div/div[2]/div/input"
    # 新建文件夹确认按钮
    New_affirm_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div/div[3]/div/div[3]/span/button[2]"
    # 新建文件夹提示信息
    New_cancel_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div/div[3]/div/div[3]/span/button[1]"

    # 邀请上传文件夹按钮
    Invite_to_upload_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div/div[1]/div[1]/button[1]"
    # 邀请上传过期时间开关
    Expiration_date_feature = By.CLASS_NAME, "el-switch__core"
    # 邀请上传过期时间输入框
    Select_Deadkube_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div/div[8]/div/div[2]/div[3]/div/div/input"
    # 邀请上传过期日期输入框（年-月-日）
    Select_date_feature = By.XPATH, "/html/body/div[3]/div[1]/div/div[1]/span[1]/div/input"
    # 邀请上传过期日期输入框（时:分:秒）
    Select_time_feature = By.XPATH, "/html/body/div[3]/div[1]/div/div[1]/span[2]/div[1]/input"
    # 邀请上传过期日期确认按钮
    Select_affirm_feature = By.CLASS_NAME, "is-plain"

    # 邀请上传邮件通知开关
    Email_notification_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div/div[8]/div/div[2]/div[3]/div[2]/div/span"
    # 邮件通知收件人输入框
    Email_send1_feature = By.CLASS_NAME, "email-tags"
    Email_send2_feature = By.CLASS_NAME, "input-new-tag"
    # 邮件通知正文输入框
    Email_text_feature = By.CLASS_NAME, "el-textarea__inner"
    # 邀请上传创建确认按钮
    upload_affirm_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div/div[8]/div/div[3]/span/button[1]"
    # 邀请上传复制链接和密码按钮
    upload_Copy_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div/div[8]/div/div[2]/div[3]/button"
    # 邀请上传关闭窗口按钮
    upload_close_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div/div[8]/div/div[3]/span/button"


    # 下载文件夹按钮
    Download_Foloer_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div/div[1]/div[1]/button[2]"
    # 下载文件按钮
    Download_files_feature = By.XPATH,"//*[@id='app']/section/main/section/section/div/div/div/div/div[1]/div[1]/button[1]"


    # 分享下载文件夹按钮
    Share_Foloer_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div/div[1]/div[1]/button[3]"
    # 分享下载文件按钮
    Share_files_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div/div[1]/div[1]/button[2]"
    # 分享下载过期时间输入框
    Share_Deadkube_feature = By.XPATH,"//*[@id='app']/section/main/section/section/div/div/div/div/div[9]/div/div[2]/div[3]/div/div/input"
    # 分享下载次数限制按钮
    Share_download_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div/div[9]/div/div[2]/div[4]/div[2]/div/span"
    # 分享下载次数输入框
    Share_num_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div/div[9]/div/div[2]/div[5]/div[2]/input"
    # 分享下载免登陆按钮
    Share_login_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div/div[9]/div/div[2]/div[6]/div[2]/div/span"
    # 分享下载通知开关按钮
    Share_notification_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div/div[9]/div/div[2]/div[7]/div[2]/div/span"
    # 分享下载创建连接按钮
    Share_affirm_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div/div[9]/div/div[3]/span/button[1]"
    # 分享下载复制链接和密码按钮
    Share_Copy_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div/div[9]/div/div[2]/div[3]/button"
    # 分享下载关闭窗口按钮
    Share_close_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div/div[9]/div/div[3]/span/button"


    # 删除文件夹按钮
    Delete_Foloer_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div/div[1]/div[1]/button[4]"
    # 删除文件按钮
    Delete_files_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div/div[1]/div[1]/button[3]"
    # 全选删除文件和文件夹按钮
    Delete_all_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div/div[1]/div[1]/button[2]"
    # 确认删除按钮
    Delete_affirm_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div/div[7]/div/div[3]/span/button[1]"


    # 复制文件按钮
    Copy_files_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div/div[1]/div[1]/button[4]"
    # 复制文件夹按钮
    Copy_Foloer_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div/div[1]/div[1]/button[5]"
    # 复制窗口-我的空间
    Copy_space_feature = By.CLASS_NAME, "el-tree-node__expand-icon"
    # 复制窗口-根目录下第二个目录
    Copy_catalogue_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div/div[5]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div/span[2]"
    # 复制窗口-确认按钮
    Copy_affirm_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div/div[5]/div/div[3]/span/button[2]"


    # 移动文件夹按钮
    Move_Foloer_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div/div[1]/div[1]/button[6]"
    # 移动文件按钮
    Move_files_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div/div[1]/div[1]/button[5]"
    # 移动多个文件或者多个文件夹
    Move_plural_feature = By.XPATH, ("//*[@id='app']/section/main/section/section/div/div/div/div/div[1]/div[1]/button[4]")
    # 移动窗口-我的空间
    Move_space_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div/div[5]/div/div[2]/div/div[1]/div[1]/div[1]/span[2]/span/i"
    # 移动窗口-我的空间第三个目录
    Move_catalogue_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div/div[5]/div/div[2]/div/div[1]/div[1]/div[2]/div[3]/div/span[2]/span"
    # 移动窗口-确认按钮
    Move_affirm_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div/div[5]/div/div[3]/span/button[2]"

    # 勾选首个文件（夹）
    Checkbox_first_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div/div[2]/div/div[3]/div/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span"
    # 全选文件（夹）
    Checkbox_all_feature = By.CLASS_NAME,"el-checkbox__inner"

    # 首个文件（夹）操作按钮
    Operation_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div/div[2]/div/div[3]/div/div[3]/table/tbody/tr/td[5]/div/div/span/i"
    # 操作-重命名按钮
    Operation_rename_feature = By.CLASS_NAME, "el-dropdown-menu__item"
    # 文件（夹）重命名输入框
    Rename_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div/div[4]/div/div[2]/div/input"
    # 重命名确认按钮
    Rename_affirm_feature = By.XPATH, "//*[@id='app']/section/main/section/section/div/div/div/div/div[4]/div/div[3]/span/button[2]"

    # 搜索输入框
    search_feature = By.CLASS_NAME, "el-input__inner"
    # 搜索图标按钮
    search_ico_feature = By.CLASS_NAME, "el-icon-search"

    # 账号信息下拉框'v'
    account_information_feature = By.XPATH, "//*[@id='app']/section/header/div/div[2]/div[1]/span"
    # 退出登录按钮
    logout_feature = By.CSS_SELECTOR, "div[class='dropdown-box-support']>span"



    # 1 我的空间菜单按钮
    def get_Space_ele(self):
        return self.get_element(self.Space_feature)

    # 2 上传
    def get_Upload_ele(self):
        return self.get_element(self.Upload_feature)

    # 2.1上传文件
    def get_Upload_files_ele(self):
        return self.get_element(self.Upload_files_feature)

    # 2.2上传文件夹
    def get_Upload_folders_ele(self):
        return self.get_element(self.Upload_folders_feature)

    # 3 新建文件夹
    def get_New_Foloer_ele(self):
        return self.get_element(self.New_Foloer_feature)

    # 3.1输入新建文件夹名称
    def get_Adirectory_name_ele(self):
        return self.get_element(self.Adirectory_name_feature)

    # 3.2点击确认按钮
    def get_New_affirm_ele(self):
        return self.get_element(self.New_affirm_feature)

    # 3.3点击取消按钮
    def get_New_cancel_ele(self):
        return self.get_element(self.New_cancel_feature)

    # 4 邀请上传(文件夹)
    def get_Invite_to_upload_ele(self):
        return self.get_element(self.Invite_to_upload_feature)

    # 4.1 链接过期时间开关设置按钮
    def get_Expiration_date_ele(self):
        return self.get_element(self.Expiration_date_feature)

    # 4.2 链接过期时间输入框
    def get_Select_Deadkube_ele(self):
        return self.get_element(self.Select_Deadkube_feature)

    # 4.3 链接过期时间年月日输入框
    def get_Select_date_ele(self):
        return self.get_element(self.Select_date_feature)

    # 4.4 链接过期时间时分秒输入框
    def get_Select_time_ele(self):
        return self.get_element(self.Select_time_feature)

    # 4.5 链接过期时间确认按钮
    def get_Select_affirm_ele(self):
        return self.get_element(self.Select_affirm_feature)

    # 4.6 邮件通知设置按钮
    def get_Email_notification_ele(self):
        return self.get_element(self.Email_notification_feature)

    # 4.7 邮件通知收件人输入框
    def get_Email1_send_ele(self):
        return self.get_element(self.Email_send1_feature)

    def get_Email2_send_ele(self):
        return self.get_element(self.Email_send2_feature)

    # 4.8 邮件通知收件内容
    def get_Email_text_ele(self):
        return self.get_element(self.Email_text_feature)

    # 4.9 邀请上传链接创建按钮
    def get_upload_affirm_ele(self):
        return self.get_element(self.upload_affirm_feature)

    # 4.10 关闭邀请上传窗口
    def get_upload_close_ele(self):
        return self.get_element(self.upload_close_feature)

    # 4.11 复制邀请上传链接和密码
    def get_upload_Copy_ele(self):
        return self.get_element(self.upload_Copy_feature)

    # 5 分享下载(文件夹)
    def get_Share_Foloer_ele(self):
        return self.get_element(self.Share_Foloer_feature)

    # 5.1 分享下载文件
    def get_Share_files_ele(self):
        return self.get_element(self.Share_files_feature)

    # 5.2 分享下载链接过期时间输入框
    def get_Share_Deadkube_ele(self):
        return self.get_element(self.Share_Deadkube_feature)

    # 5.3 分享下载链接下载次数限制按钮
    def get_Share_download_ele(self):
        return self.get_element(self.Share_download_feature)

    # 5.4 分享下载链接下载次数输入框
    def get_Share_num_ele(self):
        return self.get_element(self.Share_num_feature)

    # 5.5 分享下载链接免登陆按钮
    def get_Share_login_ele(self):
        return self.get_element(self.Share_login_feature)

    # 5.6 分享下载邮件通知设置按钮
    def get_Share_notification_ele(self):
        return self.get_element(self.Share_notification_feature)

    # 5.7 分享下载链接创建按钮
    def get_Share_affirm_ele(self):
        return self.get_element(self.Share_affirm_feature)

    # 5.10 关闭分享下载窗口
    def get_Share_close_ele(self):
        return self.get_element(self.Share_close_feature)

    # 5.11 复制分享下载链接和密码
    def get_Share_Copy_ele(self):
        return self.get_element(self.Share_Copy_feature)


    # 6 删除文件（夹）
    # 6.1全选文件（夹）
    def get_checkbox_all_ele(self):
        return self.get_element(self.Checkbox_all_feature)

    # 6.2勾选首个文件（夹）
    def get_checkbox_first_ele(self):
        return self.get_element(self.Checkbox_first_feature)

    # 6.3 点击删除按钮（文件夹）
    def get_Delete_Foloe_ele(self):
        return self.get_element(self.Delete_Foloer_feature)

    # 6.3 点击删除按钮（文件）
    def get_Delete_files_ele(self):
        return self.get_element(self.Delete_files_feature)

    # 6.4确认删除文件（夹）全选
    def get_Delete_all_ele(self):
        return self.get_element(self.Delete_all_feature)

    # 6.5确认删除文件（夹）
    def get_Delete_affirm_ele(self):
        return self.get_element(self.Delete_affirm_feature)

    # 7 重命名文件（夹）
    def get_Operation_ele(self):
        return self.get_element(self.Operation_feature)

    # 7.1点击重命名操作按钮
    def get_Operation_rename_ele(self):
        return self.get_element(self.Operation_rename_feature)

    # 7.2输入重命名文件目录名称
    def get_Rename_ele(self):
        return self.get_element(self.Rename_feature)

    # 7.3点击重命名确认按钮
    def get_Rename_affirm_ele(self):
        return self.get_element(self.Rename_affirm_feature)

    # 8 搜索文件（夹）
    def get_search_ele(self):
        return self.get_element(self.search_feature)
    # 8.1 搜索图标ico
    def get_search_ico_ele(self):
        return self.get_element(self.search_ico_feature)

    # 9 复制文件
    def get_Copy_files_ele(self):
        return self.get_element(self.Copy_files_feature)

    # 9.1 复制文件夹
    def get_Copy_Foloer_ele(self):
        return self.get_element(self.Copy_Foloer_feature)

    # 9.2 复制窗口-我的空间
    def get_Copy_space_ele(self):
        return self.get_element(self.Copy_space_feature)

    # 9.3 复制窗口-根目录下第二个目录
    def get_Copy_catalogue_ele(self):
        return self.get_element(self.Copy_catalogue_feature)

    # 9.4 复制窗口-确认按钮
    def get_Copy_affirm_ele(self):
        return self.get_element(self.Copy_affirm_feature)

    # 10 账号信息下拉框
    def get_account_information_ele(self):
        return self.get_element(self.account_information_feature)

    # 10.1 退出登录按钮
    def get_logout_ele(self):
        return self.get_element(self.logout_feature)

    # 11 移动文件（夹）
    # 11.1 移动文件夹按钮
    def get_Move_Foloer_ele(self):
        return self.get_element(self.Move_Foloer_feature)

    # 11.2 移动文件按钮
    def get_Move_files_ele(self):
        return self.get_element(self.Move_files_feature)

    # 11.3 移动多个文件或者多个文件夹按钮
    def get_Move_plural_ele(self):
        return self.get_element(self.Move_plural_feature)

    # 11.4 移动窗口-我的空间
    def get_Move_space_ele(self):
        return self.get_element(self.Move_space_feature)

    # 11.5 移动窗口-我的空间第二个目录
    def get_Move_catalogue_ele(self):
        return self.get_element(self.Move_catalogue_feature)

    # 11.6移动窗口-确认按钮
    def get_Move_affirm_ele(self):
        return self.get_element(self.Move_affirm_feature)


    # 12  下载文件（家）
    def get_Download_Foloer_ele(self):
        return self.get_element(self.Download_Foloer_feature)

    def get_Download_files_ele(self):
        return self.get_element(self.Download_files_feature)








