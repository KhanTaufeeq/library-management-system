from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class User(models.Model):

  first_name = models.CharField('First Name', blank = False, null = False, max_length=50)
  last_name = models.CharField('Last Name', blank = False, null = False, max_length=50)
  username = models.CharField('User Name', blank = False, null = False, max_length=50)
  password = models.CharField('Password', blank = False, null = False, max_length=100)
  email =    models.EmailField('Email', blank = False, null = False)
  contact = PhoneNumberField('Phone')
  created_at =  models.DateTimeField('Created At', blank = True, auto_now_add=True)
  updated_at = models.DateTimeField('Updated At', blank = True, auto_now=True)

  def __str__(self):
    return self.username