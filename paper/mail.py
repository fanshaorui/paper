from django.core.mail import send_mail
import threading
class sendmailthread(threading.Thread):
    def __init__(self,subject,body,from_mail,recipient_list):
        self.subject=subject
        self.body=body
        self.from_mail=from_mail
        self.recipient_list=recipient_list
        threading.Thread.__init__(self)
    def run(self):
        send_mail(self.subject, self.body, self.from_mail, self.recipient_list)
    
    
