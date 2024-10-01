import smtplib as s

smtpObj = s.SMTP('smtp.gmail.com',587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('yourgamil@gmail.com','password')

from_address = 'darpangaire11@gmail.com'
to_address = 'kamalgaire420@gmail.com'
message = """
Subject: Testing python

Hey bro if this email reach you just ignore it.
This is email generated my bot.
                        
                        your: Darpan Gaire
                        
"""

smtpObj.sendmail(from_address,to_address,message)

smtpObj.quit()




