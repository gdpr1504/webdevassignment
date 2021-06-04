from django.db import models

# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=40)

class record(models.Model):
    emp_id=models.IntegerField(max_length=5)
    emp_name=models.CharField(max_length=30)
    designation=models.CharField(max_length=50)
    salary=models.IntegerField(max_length=10)
    city=models.CharField(max_length=20)