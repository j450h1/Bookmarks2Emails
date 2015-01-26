# -*- coding: utf-8 -*-
"""
Created on Sun Jan 25 06:55:13 2015

@author: user
"""
import os
path = 'C:\\Users\\user\\Documents\\Python Scripts'
os.getcwd()
os.chdir(path)
os.getcwd()

#Export bookmarks file from Chrome and save as HTML
filename = 'bookmarks_1_25_15.html'
#Extract bookmarks into list
txt = open(filename)
html_doc = txt.read()
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
l = []
for link in soup.find_all('a'):
    x = link.get('href')    
    l.append(x)
    print(link.get('href'))

#Now that we have a list of all bookmarks in l:#
#Lets send one email message per bookmark

import smtplib

for message in l[140:]:

    gmail_user = "j450h1@gmail.com" #your gmail account from the sender
    gmail_pwd = "if using 2-factor authorization from Google make sure that you get a new password for this application"
    FROM = 'j450h1@gmail.com'
    TO = ['j450h1@gmail.com'] #must be a list
    SUBJECT = message
    TEXT = message

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
            """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        #server = smtplib.SMTP(SERVER) 
        server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        #server.quit()
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"


