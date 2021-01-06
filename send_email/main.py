import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

try:
    from settings import LOGIN, PASSWORD, URL
except ImportError:
    exit('DO cp settings.py.default settings.py and set token!')

def send_email():
    login = LOGIN
    password = PASSWORD
    url = URL
    toaddr = input('For: ')
    topic = input('Topic: ')
    message = input('Enter message: ')

    msg = MIMEMultipart()

    msg['Subject'] = topic
    msg['From'] = login
    body = message
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP_SSL(url, 465)
    server.login(login, password)
    server.sendmail(login, toaddr, msg.as_string())


def main():
    send_email()


if __name__ == '__main__':
    main()