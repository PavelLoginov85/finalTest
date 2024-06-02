import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
fromaddr = "address@mail.ru"
toaddr = "address@mail.ru"
mypass = "pass"
reportname = "report.xml"
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Отчет о тестировании"

with open(reportname, "rb") as f:
    part = MIMEApplication(f.read(), Name=basename(reportname))
    part['Content-Desposition'] = 'attachment; filename="%s"', basename(reportname)
    msg.attach(part)
body = "Тесты завершены"
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
server.login(fromaddr, mypass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()