from django.contrib.postgres.fields import JSONField
from django.db import models    
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
     email = models.EmailField(verbose_name='email',max_length=255, unique=True)
     phone = models.CharField(null=True, max_length=255)
     age = models.CharField(null=True, max_length=255)
     REQUIRED_FIELDS =['username','phone','first_name','last_name','age']
     USERNAME_FIELD = 'email'

     def get_username(self):
         return self.email  


class House(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    city = models.CharField(max_length=50) 
    type = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    rooms = models.IntegerField()
    beds = models.IntegerField()
    price = models.IntegerField() 
   
    def __str__(self):
        return self.title

class pickeddatesClient(models.Model):
    client = models.ForeignKey(User,on_delete=models.CASCADE)
    House = models.ForeignKey(House,on_delete=models.CASCADE)
    pickedDatesPerHouse = JSONField()


