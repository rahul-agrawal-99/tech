import re
import smtplib   # sending email
import platform

from email.mime.multipart import MIMEMultipart 

from email.mime.text import MIMEText

import datetime

import requests

from bs4 import BeautifulSoup

now = datetime.datetime.now()


res = requests.get("https://news.ycombinator.com/")   


source = res.content

soup = BeautifulSoup(source, 'html.parser')

text =  soup.find_all('tr')

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

content = f'<h1>Top News For {now.strftime("%d")}-{months[int(now.strftime("%m"))-1 ]}-20{now.strftime("%y")} </h1>'



for t in text:
    for i in str(t.text).split('\n'):
        pattern = r"\d\.\s(.+)\((.+)\)"
        news = re.findall(pattern, i)
        if len(news) > 0:
            mynews = f"<h3>{news[0][0]}</h3> By <a href='https://{news[0][1]}'> {news[0][1]} </a> <br>"
            
            content += mynews

content += f"<br> {'-'*20} <br>"
content += f"<i> This is an automated email from {platform.platform()} by Rahul. Please do not reply to this email. </i>"

#  sending mail

server = smtplib.SMTP('smtp.gmail.com', 587)

fromaddr = "SENDER'S MAIL"     # sender's email , you have turn on less secure app access in  gmail account after disabling 2 factor auth
toaddr = "RECIEVER MAIL"       # receiver's email
pas = "*******"              # sender's password


msg = MIMEMultipart()

msg["Subject"] = f'Top News Stories For {now.strftime("%d")}-{months[int(now.strftime("%m"))-1 ]}'

msg["From"] = fromaddr
msg["To"] = toaddr

msg.attach(MIMEText(content, 'html'))

server.set_debuglevel(0)  # 0 for no debugging

server.ehlo()  # say hello to the server

server.starttls()  # start TLS encryption

server.login(fromaddr, pas)  # login to the server

for i in range(10):
    server.sendmail(fromaddr, toaddr, msg.as_string())  # send the email

print("Email sent successfully")

server.quit()  # quit the server

