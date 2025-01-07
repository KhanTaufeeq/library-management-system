from django.db import models

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
