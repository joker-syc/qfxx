#发邮件的库
import smtplib
#邮件文本
from email.mime.text import MIMEText

#SMTP服务器
SMTPServer = 'smtp.163.com'

#发邮箱的地址
sender = 'zhangjiaojiao_vip@163.com'
#发送者邮箱密码：授权码
password = '1q2w3e'
#设置发送文本的内容
message = 'hello world'

#转为邮件文本
msg = MIMEText(message)
#标题
msg['Subject'] = '魔童降世'
#发送者
msg['From'] = sender

#收件人
msg['To'] ='zhangjiaojiao@163.com'

#打开SMTP服务器，端口号一般为25
mailServer = smtplib.SMTP(SMTPServer,25)
#登录邮箱
mailServer.login(sender,password)
#发送邮件
mailServer.sendmail(sender,['zhangjiaojiao_vip@163.com'],msg.as_string())
#退出邮箱
mailServer.quit()