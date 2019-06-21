from django.db import models
# Create your models here

class Commodity(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    img = models.CharField(max_length=200,blank=True,null=True)
    price = models.IntegerField(default=0)

    # user = models.ForeignKey('user.User',on_delete=models.CASCADE,blank=True,null=True)

