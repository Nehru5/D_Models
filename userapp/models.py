from django.db import models

class User(models.Model):
  name = models.CharField(max_length=200)
  email = models.EmailField()
  
  
  
class Student(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  phone = models.CharField(max_length=20)
  department = models.CharField(max_length=100)
  addrress = models.TextField()
  age = models.PositiveIntegerField(default=0)
  
  
