import smtplib

gmail_user = 'lolturcia'
gmail_passwrod = 'password'

#email properties
sent_from = gmail_user
to = ['mtrifan10@gmail.com']
email_text = 'Subject: {}\n{}'.format('Alert for reduced in price', "supp")




#email send request
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_passwrod)
    server.sendmail(sent_from, to, email_text)
    server.close()


    print ('Email sent!')
except Exception as e:
    print(e)
    print ('Something went wrong...')
