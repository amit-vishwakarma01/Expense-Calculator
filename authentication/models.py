from django.db import models

# Create your models here.

class user_detail(models.Model):
	fname=models.CharField(max_length=15)
	mname=models.CharField(max_length=15)
	lname=models.CharField(max_length=15)
	mobile=models.CharField(max_length=10)
	email=models.CharField(max_length=30)
	gender=models.CharField(max_length=100)
	password=models.CharField(max_length=30)
	salary=models.CharField(max_length=30)
class temp(models.Model):
	fname=models.CharField(max_length=15)
	mname=models.CharField(max_length=15)
	lname=models.CharField(max_length=15)
	mobile=models.CharField(max_length=10)
	email=models.CharField(max_length=30)
	gender=models.CharField(max_length=100)
	password=models.CharField(max_length=30)