from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# Tables/collections should include:
# Books (title, author, publication year, availability status).
# Users (name, contact info).
# Transactions (book ID, user ID, borrow/return date).

class Book(models.Model):

  title = models.CharField('Title', max_length=50, blank = False, null = False) 
  author = models.CharField('Author', max_length=30, blank=False, null=False)
  publication_year = models.DateField('Publication Year', blank=False, null=False)
  availability_status = models.BooleanField('Available', default = True)

  def __str__(self):
    return self.title


class Transaction(models.Model):

  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transaction')
  book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='transaction')
  borrow_date = models.DateField('Borrow Date', auto_now_add = True, blank=False, null=False)
  return_date = models.DateField('Return Date', default = None , blank = True, null=True)

  def __str__(self):
    return self.user.username