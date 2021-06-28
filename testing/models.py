from django.db import models

# Create your models here.
class Urlposting(models.Model):
    urlpost=models.CharField(max_length=100)
    timefield=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=200,default=True)
