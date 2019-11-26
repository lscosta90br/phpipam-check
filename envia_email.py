# https://pymotw.com/2/smtplib/
import smtplib
import email.utils
from email.mime.text import MIMEText

# Create the message
def envia_email(
            email_to_name, email_to, email_from_name, email_from, subj, server, debug=False):

    msg = MIMEText('This is the body of the message.')
    msg['To'] = email.utils.formataddr((email_to_name, email_to))
    msg['From'] = email.utils.formataddr((email_from_name, email_from))
    msg['Subject'] = subj

    server = smtplib.SMTP(server)
    server.set_debuglevel(debug) # show communication with the server
    try:
        server.sendmail(email_from, [email_to], msg.as_string())
    finally:
        server.quit()


envia_email(
            email_to_name = 'Leandro scosta',
            email_to = 'leandro.scosta@colaborador.inpi.gov.br',
            email_from_name = 'Leandro scosta',
            email_from = 'leandro.scosta@colaborador.inpi.gov.br',
            subj = 'Simple test message',
            server = '10.19.0.70'
            )
