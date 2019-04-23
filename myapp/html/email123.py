#coding: utf-8    
  
import smtplib    
#from email.mime.multipart import MIMEMultipart    
from email.mime.text import MIMEText    
from email.mime.image import MIMEImage 
from email.header import Header   

    
#设置smtplib所需的参数
#下面的发件人，收件人是用于邮件传输的。
smtpserver = 'smtp.1qq.com'
username = '781717725@qq.com'
password='XXX'
sender='781717725@qq.com'
#receiver='XXX@126.com'
#收件人为多个收件人
receiver=['781717725@qq.com']

subject = 'Python email test'

new_report=r"E:\myworkspace\mygit\mygitworkspace\autoAPI\myapp\report\20190418185814_TestReport.html"

with open(new_report,'r',encoding='utf8') as f:
    mail_body = f.read()

#邮箱的内容和标题
message = MIMEText(mail_body,'html','utf8')
message['Subject'] = Header(subject,charset='utf8')


#构造文字内容   
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.baidu.com"    
text_plain = MIMEText(text,'plain', 'utf-8')    
message.attach(text_plain)


#构造html
#发送正文中的图片:由于包含未被许可的信息，网易邮箱定义为垃圾邮件，报554 DT:SPM ：<p><img src="cid:image1"></p>
html = """
<html>  
  <head></head>  
  <body>  
    <p>Hi!<br>  
       How are you?<br>  
       Here is the <a href="http://www.baidu.com">link</a> you wanted.<br> 
    </p> 
  </body>  
</html>  
"""

text_html = MIMEText(html,'html', 'utf-8')
text_html["Content-Disposition"] = 'attachment; filename="texthtml.html"'   
message.attach(text_html)    



       
#发送邮件
smtp = smtplib.SMTP()    
smtp.connect('smtp.qq.com')
#我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
#smtp.set_debuglevel(1)  
smtp.login(username, password)    
smtp.sendmail(sender, receiver, msg.as_string())    
smtp.quit()
