import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from airflow.hooks.base import BaseHook
from typing import Dict

def sendEmail(**context):

    requirements,server = serverVariables()
    login = requirements['login']
    psw = requirements['psw']

    msg = context['ti'].xcom_pull(key='sendmsgEmail')
    server.ehlo()
    server.starttls()
    server.login(login, psw)

    corpo = msg
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = 'pedro_gonsalves@hotmail.com'
    email_msg['Subject'] = 'Weather Forecast with Airflow'
    email_msg.attach(MIMEText(corpo, 'plain'))

    server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
    server.quit()

def serverVariables():
    env = BaseHook.get_connection('emailLogin')

    parameters:Dict = {
        'host':env.host,
        'login':env.login,
        'psw':env.password,
        'port':env.port
    }

    server = smtplib.SMTP(host=parameters['host'],port=parameters['port'])
    print(type(server))

    return parameters, server
