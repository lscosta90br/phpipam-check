from datetime import date
from mysql.connector import Error
import ipaddress as ip
import mysql.connector
import smtplib
# criar usuario para consulta remota 
# GRANT ALL ON phpipam.* TO ipadm_remote@'192.168.2.11' IDENTIFIED BY '1q2w3e';
# systemctl list-unit-files | grep maria

#editar o arquivo de configuracao do mariadb
# vi /etc/my.cnf
# [mysqld]
# ...
# bind-address=192.168.3.117

# reinicia o servico
# systemctl restart mariadb

# systemctl stop firewalld

mydb = mysql.connector.connect(
    host="192.168.3.117",
    user="ipadm_remote",
    passwd="1q2w3e",
    database="phpipam"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT ip_addr, description, hostname, `custom_Expira-em`, state FROM ipaddresses;")

ip_addresses = mycursor.fetchall()

hoje = date.today()
dias = 0
for ip_address in ip_addresses:
    ip_addr = ip.IPv4Address(int(ip_address[0]))
    description=ip_address[1]
    hostname=ip_address[2]
    custom_expira_em=ip_address[3]
    state=ip_address[4]

    if custom_expira_em is not None:
        dias = (custom_expira_em - hoje).days
        # https://imasters.com.br/back-end/python-calculando-diferenca-de-dias-entre-duas-datas

    if dias < 0 and state == 5:
        print(f'{dias}')



#https://humberto.io/pt-br/blog/enviando-e-recebendo-emails-com-python/
# mail_from = 'origin@mail.com'
# mail_to = ['destiny1@mail.com', 'destiny2@mail.com']
# mail_subject = 'Hello'
# mail_message_body = 'Hello World!'

# mail_to_string = ', '.join(mail_to)

# mail_message = f'''
# From: {mail_from}
# To: {mail_to_string}
# Subject: {mail_subject}

# {mail_message_body}
# '''

# server = smtplib.SMTP('localhost')
# server.sendmail(mail_from, mail_to, mail_subject, mail_message)
# server.quit()