from django.db import models
from django.contrib.auth.models import User
class Requirement(models.Model):
	description=models.TextField(max_length=10000)
	creator=models.ForeignKey(User)
	createdtime=models.DateTimeField(auto_now_add=True)
	biduser=models.ManyToManyField(User,related_name="user_2")
	finish=models.BooleanField(default=False)
	prize=models.IntegerField()
	scifactor=models.IntegerField()
	def __unicode__(self):
		return self.description

