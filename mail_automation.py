import os
import smtplib
import imghdr
from email.message import EmailMessage
from getpass import getpass

user =  smtplib.SMTP_SSL('smtp.gmail.com', 465)
while True:

    if os.environ.get('EMAIL_USER') and os.environ.get('EMAIL_PASS'):
        print('Login credentials have been entered')
        email_user = os.environ.get('EMAIL_USER') 
        email_pass = os.environ.get('EMAIL_PASS')
    else:
        email_user = input("Enter your Google Username: ")
        email_pass = getpass('Enter Your Password: ')
        try:
            user.login(email_user, email_pass)
        except smtplib.SMTPAuthenticationError:
            print('Login Failure: It seems you have entered the password or username incorrects please try again')
            continue

    break       

msg = EmailMessage()
msg['Subject'] = input('Enter Subject for Email: ')
msg['From'] = email_user
#the To variable cna contain a list that will recieve th message

msg['To'] = 'javaughnmiller@gmail.com' # ex with List of Users ['javaughnmiller@gmail.com','laserman47@gmail.com', 'yvonneslyfield@yahoo.com',...]
msg.set_content('Hey I thnk your script is working if you are seeing this message. Congrats my friends :)')
#if i want to send an image
    #path of the file   
# files = ['tanjiro.png', 'tanjiro2.png', 'plans.txt']
text_input = str(input('which file do you want to send?: '))
files = [text_input]

for file in files:
    file_type=""
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name
        if imghdr.what(f.name) in ['jpg','png','jpeg','gif']:
            file_type = imghdr.what(f.name)
            
    if file_type:
        msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
    else:
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

#For later uses i want to be able to use any email server

#creating contex manager
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    # smtp.ehlo() #used to identify ourselves with the mail server we are using
    # smtpstarttls()  #used to encrypt the traffic
    # smtp.ehlo()

    smtp.login(email_user,email_pass)

    smtp.send_message(msg)

print('Your email has been sent.')
