from django.db import models

# Create your models here.

class user(models.Model):
 name=models.CharField(max_length=50)
 age=models.BigIntegerField()
 bloodgroup=models.CharField(max_length=5)
 gender=models.CharField(max_length=10)
 father_name=models.CharField(max_length=50)
 state=models.CharField(max_length=50)
 district=models.CharField(max_length=50)
 city=models.CharField(max_length=50) 
 pincode=models.BigIntegerField()
 address=models.EmailField(max_length=100,default='')
 email=models.EmailField(primary_key=True,max_length=50)
 password=models.EmailField(max_length=50)
 phone=models.BigIntegerField()
 confirm=models.CharField(max_length=20)
 date = models.DateTimeField(auto_now_add=True, null=True)
 
 
