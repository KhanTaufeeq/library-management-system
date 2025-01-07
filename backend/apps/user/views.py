from django.shortcuts import render
from . models import User 
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
import json
# Create your views here.

def signup(request):
  if request.method == 'POST':
    try:
      user_data = json.loads(request.body)
      first_name = user_data.get('first_name')
      last_name = user_data.get('last_name')
      username = user_data.get('username')
      password = user_data.get('password')
      email = user_data.get('email') 
      contact = user_data.get('contact')
    except json.JSONDecodeError:
      return JsonResponse({'error': 'Invalid json data'}, status = 400)
    
    if not first_name or not last_name or not username or not password or not email or not contact:
      return JsonResponse({'error' : 'Please fill all the details'}, status = 400)
    elif User.objects.filter(username = username).exists():
      return JsonResponse({'error': 'This username already exists'}, status = 400)
    elif User.objects.filter(email = email).exists():
      return JsonResponse({'error': 'This email already exists'}, status = 400)
    elif User.objects.filter(contact = contact).exists():
      return JsonResponse({'error': 'This phone number already exists'}, status = 400)
    else:
      user = User.objects.create(
        username = username,
        email = email,
        contact = contact,
        password = make_password(password) # hash the password
      )
      user.first_name = first_name
      user.last_name = last_name
      user.save()

      # return success response
      return JsonResponse({'message': 'Your account has been created successfully'}, status = 200)
  else:
    return JsonResponse({'error': 'Invalid request method'}, status = 405)

def signin(request):
  if request.method == 'POST':
    user_data = json.loads(request.body)
    username = user_data.get('username')
    password = user_data.get('password')

    user = authenticate(request, username = username, password = password)

    if user is not None:
      login(request, user)
      return JsonResponse({'message': 'You are successfully logged in :)', 'user_id':user.id}, status = 200)
    else:
      return JsonResponse({'error': 'No such user :('})
  else:
    return JsonResponse({'error': 'Invalid request method'}, status = 405)

def signout(request):
  logout(request)

  return JsonResponse({'message': 'You are successfully logged out :( '}) 

