from django.db import models
from require.models import Requirement
from django.contrib.auth.models import User
class Transaction(models.Model):
	requirementuser=models.ForeignKey(User,related_name="user_4")
	biduser=models.ForeignKey(User,related_name="user_5")
	requirement=models.ForeignKey(Requirement)
	start=models.DateField(auto_now_add=True)
	finish=models.BooleanField(default=False)
        pay=models.BooleanField(default=False)
	def __unicode__(self):
		return self.requirementuser.username
