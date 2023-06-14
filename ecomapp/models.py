from django.db import models

# Create your models here.
class contact_up(models.Model):
  email = models.CharField(max_length=50)
  contact = models.CharField(max_length=13)
  message = models.CharField(max_length=100)
  name = models.CharField(max_length=50)
  subject = models.CharField(max_length=50)

class User(models.Model):
  email = models.CharField(max_length=30)
  password = models.CharField(max_length=10)
  username = models.CharField(max_length=20)
  otp = models.IntegerField(default=123)
  
class Add_products(models.Model):
  user_id = models.ForeignKey(User,on_delete=models.CASCADE)
  name = models.CharField(max_length=20)
  price = models.IntegerField()
  pic = models.ImageField(upload_to='img')
  quantity = models.IntegerField(default=1)
  
  
class Add_to_cart(models.Model):
  user_id =models.ForeignKey(User,on_delete=models.CASCADE)
  product_id = models.ForeignKey(Add_products,on_delete=models.CASCADE)
  name = models.CharField(max_length=20)
  price = models.IntegerField()
  pic = models.ImageField(upload_to='img')
  quantity = models.IntegerField(default=1)
  total_price = models.IntegerField()
  
  
class Address(models.Model):
  name1 = models.CharField(max_length=30)
  email1 = models.CharField(max_length=50)
  address = models.CharField(max_length=100)
  phone = models.CharField(max_length=13)
  message = models.CharField(max_length=100)
    
  
     