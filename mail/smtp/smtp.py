'''smtp'''

from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# 输入Email地址和口令
# from_addr = input('From: ')
# password = input('Password: ')
from_addr = 'yanghaichuan@sungiant.net'
password = 'Yang321'
# 输入收件人地址
# to_addr = input('To: ')
to_addr = '248765224@qq.com'
# 输入SMTP服务器地址
# smtp_server = input('SMTP server: ')
smtp_server = 'smtp.exmail.qq.com'

# 邮件对象:
msg = MIMEMultipart('alternative')
# 邮件正文是MIMEText:
msg.attach(MIMEText('Hello', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))
# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('test.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是jpg类型:
    mime = MIMEBase('image', 'jpg', filename='test.jpg')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='test.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('沐水杉 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候......', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.starttls()
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()