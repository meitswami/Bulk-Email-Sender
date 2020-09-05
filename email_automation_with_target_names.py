#single sender, multiple recievers with individual names

import smtplib
from itertools import cycle
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import gmtime, strftime
import time


def get_targets(filename):
    #global target_email
    target_email = []

    with open(filename, mode='r', encoding='utf-8') as target_file:
        for line in target_file:
            target_email.append(line.split()[0])

    return target_email


def get_target_names(filename):

    target_name = []

    with open(filename, mode='r', encoding='utf-8') as target_name_file:
        for line in target_name_file:
            target_name.append(line.split()[0])

    return target_name


def main():

    sender_email = 'abc@abc.com'
    sender = 'ABC <abc@abc.com>'
    password = 'abcde@12345'
    target_email = get_targets('to.txt')
    target_name = get_target_names('reciever_names.txt')

    file=open('body.txt', 'r')   #define email body
    body=file.read()


    zip_list = zip(target_email, target_name)

    for email_t, name_t in zip_list:

        # set up the SMTP server
		# set up gmail
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
		#set up yandex



        s.starttls()
        print ("loging in",sender)
        s.login(sender_email, password)

        msg = MIMEMultipart()       #create a message

        # setup the parameters of the message
        msg['From']=sender
        print('sending from', sender_email)
        msg['To']=email_t
        print('sending to', email_t)

        msg['Subject']="This is TEST"
        # add in the message body
        msg.attach(MIMEText('Dear'+' '+name_t, 'plain'))
        msg.attach(MIMEText(body, 'plain'))

        # send the message via the server set up earlier.
        s.send_message(msg)
        print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
        s.quit()
        time.sleep(5)
if __name__ == '__main__':
    main()
