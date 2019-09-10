#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# add to crontab by:
# @reboot /usr/bin/python3 /home/dl/report_ip.py


import time
import os
import socket
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = 'dwSun@mail.com.cn'    # 发件人邮箱账号
my_pass = 'dwSunMailBoxPass'              # 发件人邮箱密码
my_user = 'dwSun@mail.com.cn'      # 收件人邮箱账号，我这边发送给自己


time.sleep(30)

text = '\n'.join(os.popen('ip addr'))


def mail():
    ret = True
    try:
        msg = MIMEText(text, 'plain', 'utf-8')
        # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['From'] = formataddr([socket.gethostname(), my_sender])
        # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['To'] = formataddr(["dwSun", my_user])
        msg['Subject'] = "IP report"                # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL(
            "smtp.mail.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.sendmail(my_sender, [my_user, ], msg.as_string())
        server.quit()  # 关闭连接
        list(os.popen('echo $(date) 邮件发送成功 >>~/.ip_log'))
    except Exception as ex:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        list(os.popen('echo $(date) 邮件发送失败 >>~/.ip_log'))
        list(os.popen('echo $(date) {} >>~/.ip_log'.format(ex)))
        ret = False
    return ret


mail()


