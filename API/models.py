from django.db import models

# Create your models here.

class BaseForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_No = models.CharField(max_length=12)
    city = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class OurBusiness(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_No = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    message = models.TextField(max_length=300)
    
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=300)
    
    def __str__(self):
        return self.name
       
