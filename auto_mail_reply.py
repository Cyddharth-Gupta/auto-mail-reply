#-*- coding:UTF-8 -*-
__author__ = nodejx

import imaplib, email, smtplib, time

server = "mail.test.com"
fadd =  "admin@test.com"
mbody = ["""This is an example!"""]

while True:
    i = imaplib.IMAP4(server, 143)
    i.login("admin", "passwd")
    i.select("INBOX")
    types, datas = i.search(None, "NEW")
    ids = datas[0]
    
    if ids == "":
        i.logout()
	pass
    else:
        for n in ids.split():
	    typs, dats = i.fetch(n, '(RFC822)')
	    for dat in dats:
	        if isinstance(dat, tuple):
	            rmsg = email.message_from_string(dat[1])
	            msub = rmsg['subject']
	            mfro = rmsg['from'].replace("<", '').replace(">",'').split()[-1]
                    if (mfro == "test1@test.com") or (mfro == "test2@test.com"):
                        pass
                    else:
	                mhead = ['From:%s' % fadd, 'To:%s' % mfrom ,'Subject:%s' % msub]		
	                smsg = "\r\n\r\n".join(['\r\n'.join(mhead), '\r\n'.join(mbody)])
	                s = smtplib.SMTP()
                        s.connect(server)
	                s.starttls()
	                s.login("admin", "passwd")
                        s.sendmail(fadd, mfro, smsg)
                        print "Send to %s success!" % mfro
	                s.quit()
    time.sleep(120)