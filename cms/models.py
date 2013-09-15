from django.db import models
class friendlink(models.Model):
    name=models.CharField(max_length=140)
    link=models.CharField(max_length=300)
    def __unicode__(self):
        return self.name
