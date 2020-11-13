import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.ehlo()

server.login('sender@gmail.com','password')

subject = 'Email subject'
text = 'this is an email text'

msg = f"Subject: {subject}\n{text}"

server.sendmail('sender@gmail.com','receiver@gmail.com',msg)
print("email successfully sent!")
server.quit()
