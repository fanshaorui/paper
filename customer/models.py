from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
	user=models.ForeignKey(User,related_name="user_0",unique=True)
	phonenumber=models.DecimalField(max_digits=15,decimal_places=0)
	def __unicode__(self):
		return self.user.username

# Create your models here.
