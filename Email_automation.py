import smtplib
from itertools import cycle
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import gmtime, strftime
import time

def get_senders(filename):
    #global sender_email
    sender_email = []
    #global password
    password = []
    with open(filename, mode='r', encoding='utf-8') as sender_file:
        for line in sender_file:
            sender_email.append(line.split()[0])
            password.append(line.split()[1])
    return sender_email, password

def get_targets(filename):
    #global target_email
    target_email = []

    with open(filename, mode='r', encoding='utf-8') as target_file:
        for line in target_file:
            target_email.append(line.split()[0])

    return target_email



def main():


    sender_email, password = get_senders('from.txt')
    target_email = get_targets('to.txt')

    file=open('body.txt', 'r')   #define email body
    body=file.read()

    zip_list = zip(target_email, cycle(sender_email),cycle(password)) if len(target_email) > len(sender_email) else zip(target_email, sender_email,password)


    for email_t, email_s,passwd in zip_list:

        # set up the SMTP server
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        print ("loging in",email_s)
        s.login(email_s, passwd)

        msg = MIMEMultipart()       #create a message

        # setup the parameters of the message
        msg['From']=email_s
        print('sending from', email_s)
        msg['To']=email_t
        print('sending to', email_t)

        msg['Subject']=""
        # add in the message body
        msg.attach(MIMEText(body, 'html'))

        # send the message via the server set up earlier.
        s.send_message(msg)
        print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
        s.quit()
        time.sleep(186)
if __name__ == '__main__':
    main()
