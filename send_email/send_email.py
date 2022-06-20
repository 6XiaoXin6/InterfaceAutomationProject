#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" 四步走"""

__author__ = 'List.Xie'

import smtplib
from email.header import Header
from email.mime.text import MIMEText

from my_log.my_Logger import MyLogger

log=MyLogger().getMyLogger()
class MyEmail():
    def __init__(self, *args):
        self.receiver = args

    server = "smtp.163.com"

    sender = "xyz307322186@163.com"
    password = "CWWOCWGHYEXUXXHN"

    # receiver = ["2585174552@qq.com", "xiexinli6@163.com"]
    def send_email(self):

        with open("C:/Users/xiaoxin/PycharmProjects/InterfaceAutomationProject/test_reports/reports_html/report.html", "rb") as f:
            text = f.read()
        msg = MIMEText(text, "html", "utf-8")
        msg["Subject"] = Header("接口测试报告", "utf-8")

        stp = smtplib.SMTP(self.server)
        stp.set_debuglevel(1)
        try:
            stp.login(self.sender, self.password)
            stp.sendmail(self.sender, self.receiver, msg.as_string())
        except Exception as e:
            log.exception(e)
        finally:
            stp.quit()
