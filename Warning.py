import smtplib
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from datetime import datetime
import os

class Alert:
    
    def __init__(self, type : str, to_addr = None, data : tuple(), server = 'smtp.gmail.com:587', provider = None):
        '''Creates a Warning that results in certain actions being taken'''
        #TODO Add in urgency
        self.type = type
        self.data = data
        pic_name = data[0].splitext()[0]
        self.from_addr = ('osorioaj@uci.edu', 'D@nk@nt3@t3R')
            #Send SMS immediately with important data based on message
        
        if pic_name.startswith('unknown'):
            message = 'At ' + str(datetime.fromtimestamp(os.stat(self.data[0]).st_ctime)) + ' a stranger was spotted on the premises./n/n\
            They will remain on your blacklist unless identified and manually cleared for your whitelist./n/nTheir picture is below./n/nThey\
            have been labeled as ' + pic_name
            msg = MIMEMultipart()
            msg.attach(MIMEText(message))
            msg.attach(MIMEImage(self.data[0].read()))
            if self.type == 'SMS':
                Alert.sendemail(self.from_addr[0], to_addr, '', 
                      "Alert! Stranger(s) On Premises!", msg,
                      self.from_addr[0], self.from_addr[1], self.data[0])
            else:
                Alert.sendemail(self.from_addr[0], None, '', 
                      "Alert! Stranger(s) On Premises!", msg,
                      self.from_addr[0], self.from_addr[1], self.data[0])
        elif data[1] and not pic_name.startswith('unknown'):
            message = 'At ' + str(datetime.fromtimestamp(os.stat(self.data[0]).st_ctime)) + ' a blacklisted person, known as ' + pic_name + ', was\
            spotted on the premises./n/nThey will remain on your blacklist unless manually cleared for your whitelist./n/nTheir picture is below.'
            msg = MIMEMultipart()
            msg.attach(MIMEText(message))
            msg.attach(MIMEImage(self.data[0].read()))
            Alert.sendemail(self.from_addr[0], to_addr, '',
                  "Alert! Blacklisted Person(s) On Premises!", msg,
                  self.from_addr[0], self.from_addr[1], self.data[0])
        else:
            message = 'At ' + str(datetime.fromtimestamp(os.stat(self.data[0]).st_ctime)) + pic_name + ' was spotted on the premises./n/n\
            Their picture is below.'
            msg = MIMEMultipart()
            msg.attach(MIMEText(message))
            msg.attach(MIMEImage(self.data[0].read()))
            Alert.sendemail(self.from_addr[0], to_addr, '',
                  "Alert! New Presence On Premises!", msg,
                  self.from_addr[0], self.from_addr[1], self.data[0])  
                  
    
    @staticmethod
    def sendemail(from_addr, to_addr_list, cc_addr_list,
                  subject, message,
                  login, password,
                  smtpserver='smtp.gmail.com:587'):
        header  = 'From: %s\n' % from_addr
        header += 'To: %s\n' % ','.join(to_addr_list)
        header += 'Cc: %s\n' % ','.join(cc_addr_list)
        header += 'Subject: %s\n\n' % subject
        message = header + message
        server = smtplib.SMTP(smtpserver)
        server.starttls()
        server.login(login,password)
        problems = server.sendmail(from_addr, to_addr_list, message)
        server.quit()
        return problems
    
# Alltel
# [10-digit phone number]@sms.alltelwireless.com
# Example: 2125551212@sms.alltelwireless.com
# 
# AT&T Wireless (formerly Cingular)
# [10-digit phone number]@txt.att.net
# Example: 2125551212@txt.att.net
# 
# For multimedia (picture and video) messages, use [10-digit-number]@mms.att.net
# Example: 2125551212@mms.att.net
# 
# Boost Mobile
# [10-digit phone number] @sms.myboostmobile.com
# Example: 1234567890@sms.myboostmobile.com
# 
# Cricket Wireless
# [10-digit phone number]@sms.mycricket.com
# Example: 1234567890@sms.mycricket.com
# 
# For multimedia messages: [10-digit phone number]@mms.mycricket.com
# Example: 1234567890@mms.mycricket.com
# 
# Sprint
# [10-digit phone number]@messaging.sprintpcs.com
# Example: 2125551234@messaging.sprintpcs.com
# 
# T-Mobile
# [10-digit phone number]@tmomail.net
# Example: 4251234567@tmomail.net
# 
# Tracfone or Straight Talk
# The address varies. Click this link to find out how to discover yours.
# 
# Verizon
# [10-digit-number]@vtext.com
# Example: 9495551212@vtext.com
# 
# Virgin Mobile USA
# [10-digit phone number] @vmobl.com
# Example: 5551234567@vmobl.com
