from django.urls import path 
from . import views

urlpatterns = [
    path('', views.list_books, name = "list books"),
    path('add/', views.add_book, name = "add book"),
    path('update/<int:book_id>/', views.update_book, name = "update book"),
    path('delete/<int:book_id>/', views.delete_book, name = "delete book"),
    path('borrow/', views.borrow_book, name = 'borrow book'),
    path('update_availability/<int:book_id>/', views.update_book_availability, name = "update availability"), 
    path('available_books/', views.list_available_books, name = 'list available books'),
    path('return/', views.return_book, name = "return book")
]
