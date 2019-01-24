import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def sendEmail(subject, message, picURI, filename):
    email_user = 'hipor014@gmail.com'
    email_send = 'hipor014@gmail.com'
    email_password = 'S28991410V'

    msg = MIMEMultipart()
    msg['From'] = "AIY<"+email_user+">"
    msg['To'] = email_send
    msg['Subject'] = subject

    # 信件內容
    body = message
    msg.attach(MIMEText(body, 'plain', 'UTF-8'))
    # 信件附件
    attachment = open(picURI, 'rb')
    part = MIMEBase('image', 'jpeg; name= "'+ filename+'"')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename= "' + filename+'"')

    msg.attach(part)
    text = msg.as_string()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, email_password)

    message = "Test to sen email from Python"
    server.sendmail(email_user, email_send, text)
    server.quit()
