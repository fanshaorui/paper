from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
	user=models.ForeignKey(User,related_name="user_1",unique=True)
	phonenumber=models.IntegerField(blank=True)
	realname=models.CharField(max_length=140)
	selfdescription=models.TextField(max_length=10000)
        bankaccount=models.IntegerField()
        bank=models.CharField(max_length=140)
	def __unicode__(self):
		return self.realname
