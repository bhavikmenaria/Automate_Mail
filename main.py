import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


from_addr='yashmenariabhavik@gmail.com'
to_addr=['menariabhavik@gmail.com']
msg=MIMEMultipart()
msg['From']=from_addr
msg['To']=" ,".join(to_addr)
msg['subject']='just to check'

body='welcome to this universe'

msg.attach(MIMEText(body,'plain'))

email='2023pcecsbhavik037@poornima.org'
password='yashmen@6'

mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login(email,password)
text=msg.as_string()
mail.sendmail(from_addr,to_addr,text)
mail.quit()