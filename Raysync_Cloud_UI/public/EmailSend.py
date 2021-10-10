# -*- comding:utf-8   -*-

import logging
import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import config
import time,os
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr
from bs4 import BeautifulSoup


# aXbAWHc2C5KCWx2R
pwd = os.path.dirname(os.path.abspath(__file__))
print()
def emailsend():
    '''发送自动化报告到指定邮箱'''
    sender = '18126480338@163.com'  # 发件人邮箱
    receivers = [
        # 'zuowangwang@rayvision.com',
        # 'halley@rayvision.com',
        # 'loujian@rayvision.com',
        # 'amber@rayvision.com',
        # 'beyond_lee@rayvision.com',
        # 'rachelxiao@rayvision.com'，
        # 'caojing@rayvision.com'
    ]
    # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    # receivers = ['halley@rayvision.com','rachelxiao@rayvision.com']
    receivers = '1402430303@qq.com'

    #发件人的账号和授权密码
    mail_user = "18126480338@163.com"
    mail_pass = "MMPCJNRVZSMJUWME"

    #发件人邮箱服务
    mail_host = "smtp.163.com"


    #读取报告文件内容放到邮件当中
    now = time.strftime('%Y-%m-%d')
    path = config.BASE_DIR+'/report/' + 'html/'+'index.html'
    f = open(path, 'rb')
    mail_body = f.read()
    f.close()

    # #读取报告指定行数来判断传参
    # soup = BeautifulSoup(open(path, 'rb'),'lxml')
    # a = str(soup.select('#total_row'))
    # percent = a.split('\n')[-2].replace("<td>" ,"").replace("</td>" ,"")

    message = MIMEMultipart()
    message['From'] = Header("test发件人", 'utf-8')  # 发件人
    message['To'] = Header('test收件人', 'utf-8')  # 收件人姓名
    subject = 'test标题'    # 邮件标题
    message['Subject'] = Header(subject, 'utf-8').encode()
    msgAlternative = MIMEMultipart('alternative')
    message.attach(msgAlternative)


    mail_msg = """
    <h1><font size="5" coor="black">如果要查看具体详情请下载HTML附件，即可展开查看详情</font></h1>
    """

    msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
    msgAlternative.attach(MIMEText(mail_body, 'html', 'utf-8'))


    now = time.strftime('%Y-%m-%d')        #定义时间变量
    # 构造附件1，传送当前目录下的 test.txt 文件
    fujian1 = MIMEText(open((config.BASE_DIR)+'/log/' + 'test.log', 'rb').read(), 'base64', 'utf-8')
    fujian1["Content-Type"] = 'application/octet-stream'
    fujian1["Content-Disposition"] = 'attachment; filename="%s.txt"'% now # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    message.attach(fujian1)


    # 构造附件2，传送当前目录下的 .html 文件
    fujian2 = MIMEText(open((config.BASE_DIR)+'/report/' + 'html/'+ 'index.html', 'rb').read(), 'html', 'utf-8')
    fujian2["Content-Type"] = 'application/octet-stream'
    fujian2["Content-Disposition"] = 'attachment; filename="%s.html"' % now
    message.attach(fujian2)

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        logging.info("-------邮件发送成功-------")


    except smtplib.SMTPException:
        logging.info("************Error: 邮件发送失败************")

