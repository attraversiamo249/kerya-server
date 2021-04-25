from django.contrib.postgres.fields import JSONField
from django.db import models    
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
     picture = models.ImageField(null=True, blank=True)
     email = models.EmailField(verbose_name='email',max_length=255, unique=True)
     phone = models.CharField(null=True, max_length=255)
     REQUIRED_FIELDS =['username','phone','first_name','last_name']
     USERNAME_FIELD = 'email'

     def get_username(self):
         return self.email  


class House(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    city = models.CharField(max_length=50) 
    daira = models.CharField(max_length=50, default="empty") 
    type = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    rooms = models.IntegerField()
    kitchen = models.BooleanField()
    bathroom = models.BooleanField()
    price = models.IntegerField()
    description = models.TextField()
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    image4 = models.ImageField(null=True, blank=True)
    image5 = models.ImageField(null=True, blank=True)



class Dates(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    house = models.ForeignKey(House,on_delete=models.CASCADE)
    dates = JSONField()



