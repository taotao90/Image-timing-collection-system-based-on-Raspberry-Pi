# coding=utf-8
import smtplib
import os
from email.mime.text import MIMEText
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
 
msg_from = 'xxxx@qq.com'  # 发送方邮箱
passwd = 'xxxxxx'  # 填入发送方邮箱的授权码'zclcyrowxbqsbgej' 
msg_to = 'xxxx@qq.com'  # 收件人邮箱
 
def send():
    
    dd = os.popen('echo "get battery" | nc -q 0 127.0.0.1 8423')
    rr = dd.read()
    print(rr)
    ret=True
    subject = '%s'%rr  # 主题
    msg = MIMEMultipart('related')
    content = MIMEText('<html><body><img src="cid:imageid" alt="imageid"></body></html>', 'html', 'utf-8')  # 正文
    # msg = MIMEText(content)
    msg.attach(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
 
    file = open("/home/pi/camera/image.jpg", "rb")
    img_data = file.read()
    file.close()
 
    img = MIMEImage(img_data)
    img.add_header('Content-ID', 'imageid')
    msg.attach(img)
 
    try:
        
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 邮件服务器及端口号
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        s.quit()
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret=False
    return ret
 
ret=send()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")
