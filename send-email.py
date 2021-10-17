# SMTP object is used for the email transfer
import  smtplib
import getpass

sender_mail = 'harishgvt@gmail.com'
receivers_mail = 'harish.gsh22@gmail.com'

message = """From: From Person %s
To: To Person %s
Subject: Sending SMTP e-mail
This is a test e-mail message.
"""%(sender_mail,receivers_mail)

# Using getpass module to get the password and then send the email using sendemail method of smtplib.
try:
    password = getpass.getpass()
    smtpObj = smtplib.SMTP("gmail.com", 587)
    smtpObj.login(sender_mail,password)
    smtpObj.sendmail(sender_mail, receivers_mail, message)
    print("Successfully sent email")
except Exception:
    print("Error: unable to send email")

