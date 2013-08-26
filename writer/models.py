from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
	user=models.ForeignKey(User,related_name="user_1",unique=True)
	phonenumber=models.DecimalField(max_digits=15,decimal_places=0)
	realname=models.CharField(max_length=140)
	selfdescription=models.TextField(max_length=10000)
        bankaccount=models.DecimalField(max_digits=20,decimal_places=0)
        bank=models.CharField(max_length=140)
	def __unicode__(self):
		return self.realname
