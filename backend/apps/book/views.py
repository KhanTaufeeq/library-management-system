from django.shortcuts import render
from . models import Book
from django.contrib.auth.models import User
from . models import Transaction
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import now
import json

# Create your views here.

# CRUD operations on books (add, update, delete, view).
# Borrow and return functionality.
# Listing books by availability.

@login_required
@csrf_exempt
def list_books(request):
  if request.method == 'GET':
    books = list(Book.objects.values('id', 'title', 'author', 'publication_year', 'availability_status')) 
    return JsonResponse(books, safe=False)
  else:
    return JsonResponse({"error":"Invalid request method"}, status = 405)
  

@csrf_exempt
@login_required
def list_available_books(request):
  if request.method == 'GET':
      books = list(Book.objects.values('id', 'title', 'author', 'publication_year', 'availability_status')) 
      available_books = []
      for i in books:
        if i["availability_status"] == True:
          available_books.append(i)
        else:
          continue
      return JsonResponse(available_books, safe=False)
  else:
    return JsonResponse({"error": "Invalid request method"}, status = 405)



@csrf_exempt
@login_required
def add_book(request):

  if request.method == 'POST':
    try:
      book_data = json.loads(request.body)
      title = book_data.get('title')
      author = book_data.get('author')
      publication_date = book_data.get('publication_year')
      availability = book_data.get('availability_status')
    except json.JSONDecodeError:
      return JsonResponse({"error": "Invalid json data"}, status = 400)
    
    book = Book.objects.create(
      title = title, 
      author = author, 
      publication_year = publication_date, 
      availability_status = availability
    ) 
    if request.user.is_staff:
      book.save()
    else:
      return JsonResponse({"error": "You don't have permission to add book details in library"}, status = 403)
    return JsonResponse({"message": f"{title} book has been added successfully"}, status = 200) 
  else:
    return JsonResponse({"error": "Invalid request method"}, status = 400)


@login_required
@csrf_exempt
def update_book(request, book_id):
  if request.method == 'PUT':
    try:
      books = json.loads(request.body) 
      title = books.get('title')
      author = books.get('author')
      publication_year = books.get('publication_year')
      availability = books.get('availability_status')

      book = Book.objects.get(id = book_id)

      if request.user.is_staff:
        if title:
          book.title = title
        elif author:
          book.author = author
        elif publication_year:
          book.publication_year = publication_year
        elif availability is not None:
          book.availability_status = availability 

        book.save()
        return JsonResponse({"message": f"{book.title} book has been updated successfully"}, status = 200)
      
      else:
        return JsonResponse({"error": "You don't have access to update a book in library"}, status = 403)
    
    except Book.DoesNotExist:
      return JsonResponse({"error" : "Book not found"}, status = 404)
    
  else:
    return JsonResponse({"error": "Invalid request method"}, status = 405)
  

@login_required
@csrf_exempt
def delete_book(request, book_id):
  if request.method == 'DELETE':
    try:
      book = Book.objects.get(id = book_id)
      if request.user.is_staff:
        book.delete()
        return JsonResponse({"message": "Book has been deleted successfully"}, status = 200)
      else:
        return JsonResponse({"error" : "You don't have permission to delete a book from library"}, status = 403)
    except Book.DoesNotExist:
      return JsonResponse({"error": "Book not found"}, status = 404)
  else:
    return JsonResponse({"error": "Invalid request method"}, status = 405)
  

@login_required
@csrf_exempt
def borrow_book(request):
  if request.method == 'POST':
    try:
      transaction_data = json.loads(request.body)
      user_id = transaction_data.get('user_id')
      book_id = transaction_data.get('book_id') 

      if not user_id or not book_id:
        return JsonResponse({"error" : "Both user id and book id are required"}, error = 400)
      
      try:
        user = User.objects.get(id = user_id)
      except User.DoesNotExist:
        return JsonResponse({"error" : "User does not found"}, status = 404) 
      
      try:
        book = Book.objects.get(id = book_id)
      except Book.DoesNotExist:
        return JsonResponse({"error" : "Book does not found"}, status = 404) 
      
      if book.availability_status == False:
        return JsonResponse({"error" : "Sorry, this book is not available"}, status = 400)  

      transaction = Transaction.objects.create(
        user = user,
        book = book,
        borrow_date = now()
      )

      book.availability_status = False
      book.save()

      transaction.save()
      return JsonResponse({"message": "The transaction is done successfully"}, status = 200)
    
    except json.JSONDecodeError:
      return JsonResponse({"error" : "Invalid JSON responsive"}, status = 400)
    
  else:
    return JsonResponse({"error": "Invalid request method"}, status = 405)
  

@csrf_exempt
@login_required
def return_book(request):
  if request.method == 'POST':
    try:
      transaction_data = json.loads(request.body)
      transaction_id = transaction_data.get('transaction_id')

      if not transaction_id:
        return JsonResponse({"error": "Transaction ID is required"}, status = 400)

      transaction = Transaction.objects.get(id = transaction_id)

      if transaction.return_date is not None:
        return JsonResponse({"error": "This book has already been returned"}, status = 400)
      
      book = transaction.book
      book.availability_status = True
      book.save()

      transaction.return_date = now() 
      transaction.book.availability_status = True 

      transaction.save()
      return JsonResponse({"message": "Book has been return successfully"}, status = 200)
    
    except json.JSONDecodeError:
      return JsonResponse({"error": "Invalid JSON responsive"}, status = 400) 
    
  else:
    return JsonResponse({"error" : "Invalid request method"}, status = 405)



@login_required
@csrf_exempt
def update_book_availability(request, book_id):

  if request.method == 'PUT':
    try:
      book = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
      return JsonResponse({"error" : "Book does not found"}, status = 404)
    
    if request.user.is_staff:
      if book.availability_status == False:
        book.availability_status = True 
        book.save()
      else:
        book.availability_status = False 
        book.save()
    else:
      return JsonResponse({"error": "You don't have access to updated book's availability"}, status = 403)

    return JsonResponse({"message" : f"{book.title}'s availability has been updated"}, status = 200)
  else:
    return JsonResponse({"error" : "Invalid request method"}, status = 405) 
