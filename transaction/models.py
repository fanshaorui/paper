from django.db import models
from require.models import Requirement
from django.contrib.auth.models import User
import datetime
import time
class Transaction(models.Model):
	requirementuser=models.ForeignKey(User,related_name="user_4")
	biduser=models.ForeignKey(User,related_name="user_5")
	requirement=models.ForeignKey(Requirement,unique=True)
	start=models.DateField(auto_now_add=True)
	finish=models.BooleanField(default=False)
        pay=models.BooleanField(default=False)
        order_id=models.CharField(max_length=140)
	def __unicode__(self):
		return self.requirementuser.username
        def save_order(self,):
            number=time.strftime("%Y%m%d", time.localtime())+str(self.requirement.id)+time.strftime("%H%M%S", time.localtime())
            self.order_id=number
            super(Transaction,self).save()

            
        
