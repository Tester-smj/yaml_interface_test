#coding=utf-8
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendMail():
      sender = 'xxx@xxx.cn'
      receiver ='xxx@xxx.cn'
      subject=u'[下单平台]接口自动化测试报告通知'
      smtpserver='smtp.exmail.qq.com'
      username='xxx@xxx.cn'
      password='xxxx'

      msg = MIMEMultipart('related')
      msg['Subject'] = subject
      msg['From'] = sender
      msg['To'] = ''.join(receiver)

      #构造附件
      path = 'F:\\test\\study\\yaml\\report.html'
      att = MIMEText(open(path, 'rb').read(), 'base64', 'utf-8')
      att["Content-Type"] = 'application/octet-stream'
      att["Content-Disposition"] = 'attachment; filename="report.html"'
      msg.attach(att)

      smtp = smtplib.SMTP()
      smtp.connect(smtpserver)
      smtp.login(username, password)
      logging.info(u'邮件发送成功！')
      smtp.sendmail(sender, receiver, msg.as_string())
      smtp.quit()