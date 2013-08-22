from django.db import models
class writerExample(models.Model):
    name=models.CharField(max_length=140)
    degree=models.CharField(max_length=140)
    university=models.CharField(max_length=140)
    income=models.CharField(max_length=250)
    def __unicode__(self, ):
        return self.name
    
class customerExample(models.Model):
    price=models.CharField(max_length=140)
    sci=models.CharField(max_length=140)
    require=models.CharField(max_length=250)
    def __unicode__(self, ):
        return self.require