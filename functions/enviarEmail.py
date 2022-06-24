from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from functions.lerConfig import ler_json
import smtplib
import logging
import time


class EnviarEmail():
    
    def __init__(self,):
        self.conf = ler_json('credentials.json')
        self.log = logging.getLogger('root')
        self.servidor = self.conf[0]['servidor_email_remetente']
        self.porta = self.conf[0]['porta_email_remetente']
        self.log = logging.getLogger(name="root")
        

    def enviaremail(self, emaildest, assunto, remetente, senha, corpo_Email):
        self.log.info("Enviando email para {}".format(emaildest))
        
        try:

            server = smtplib.SMTP(self.servidor, self.porta)
            server.ehlo()
            server.starttls()
            server.login(remetente, senha)
            message = corpo_Email
            email_msg = MIMEMultipart()
            email_msg['From'] = remetente
            email_msg['To'] = emaildest
            email_msg['Subject'] = assunto
            email_msg.attach(MIMEText(message, 'plain'))
            server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
            server.quit()
            return True
        except smtplib.SMTPRecipientsRefused as err:
            return err
        except Exception as erro:
            self.log.exception(erro)
