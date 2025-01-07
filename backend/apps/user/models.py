from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

# Create your models here.
class MyUser(models.Model):

  user = models.OneToOneField(User, on_delete=models.CASCADE)
  contact = PhoneNumberField('Phone')
  created_at =  models.DateTimeField('Created At', blank = True, auto_now_add=True)
  updated_at = models.DateTimeField('Updated At', blank = True, auto_now=True)

  def __str__(self):
    return self.user.username 