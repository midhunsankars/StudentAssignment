from django.db import models

# Create your models here.

class Register(models.Model):
   name = models.CharField(max_length=200)
   dob = models.DateField()
   phone = models.CharField(max_length=200)
   username = models.CharField(max_length=200)
   password = models.CharField(max_length=200)
   image = models.ImageField()
   type = models.CharField(max_length=200)

   class Meta:
       db_table = 'Register'
