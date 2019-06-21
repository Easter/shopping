from django.db import models
from django.utils.six import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class User(models.Model):
    username = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=255,default='xxx@xxx.xxx')
    def __str__(self):
        return self.username


class User_commodity(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    commodity = models.ForeignKey('shopping.Commodity',on_delete=models.CASCADE)
    number = models.IntegerField(default=1)
