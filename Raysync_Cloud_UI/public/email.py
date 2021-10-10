# -*-coding:GBK -*-

sender = "18126480338@163.com"
receivers = "1402430303@qq.com"
mail_host = "smtp.163.com"
mail_user = "18126480338@163.com"
mail_pass = "MMPCJNRVZSMJUWME"
subject = "Raysync_Cloud"

import smtplib
import time
import config
import logging
from email.mime.text import MIMEText  # 发送正文
from email.mime.multipart import MIMEMultipart  # 发送多个部分
from email.mime.application import MIMEApplication  # 发送附件
from email.header import Header  # 从email包引入Header()方法，是用来构建邮件头

def email():

    now = time.strftime('%Y-%m-%d')
    # 构造一个邮件体：正文、附件
    msg = MIMEMultipart()  # 邮件体
    msg['From'] = sender  # 发件人
    msg['To'] = receivers  # 收件人
    tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))  # 获取系统时间
    msg['Subject'] = Header(subject + '_' + tm, 'utf-8')  # 邮件主题

    # 构建正文
    content = """
                             执行测试中……
                             测试已完成！！
                             生成报告中……
                             报告已生成……
                             报告已邮件发送！！
                            """
    email_body = MIMEText(content, 'plain', 'utf-8')
    msg.attach(email_body)

    # 将正文添加到邮件体中
    # 构建附件
    att = MIMEText(open((config.BASE_DIR)+'/report/' + 'html/'+ 'index.html', 'rb').read(), 'html', 'utf-8')  # 打开附件
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="%s.html"' % now
    msg.attach(att)  # 添加附件到邮件体中

    try:
        smtpObj = smtplib.SMTP()
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 使用smtp协议发送邮件，SSL协议来进行加密传输，465为端口号
        smtpObj.login(mail_user, mail_pass)  # 邮箱登录
        smtpObj.sendmail(sender, receivers, msg.as_string())  # 发送邮件
        logging.info('send mail OK')
        smtpObj.quit()

    except smtplib.SMTPException:
        logging.info('send mail Fail')