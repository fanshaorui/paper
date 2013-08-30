from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
    description=models.CharField(max_length=250)
    title=models.CharField(max_length=250)
    def __unicode__(self):
        return self.title
class Requirement(models.Model):
	description=models.TextField(max_length=10000)
	creator=models.ForeignKey(User)
	createdtime=models.DateTimeField(auto_now_add=True)
	biduser=models.ManyToManyField(User,related_name="user_2")
	finish=models.BooleanField(default=False)
	prize=models.IntegerField()
	scifactor=models.IntegerField()
        theme=models.CharField(max_length=140)
        circle_min=models.IntegerField()
        circle_max=models.IntegerField()
        category=models.ManyToManyField(Category,related_name="category_2",blank=True)
	def __unicode__(self):
		return self.description

    


