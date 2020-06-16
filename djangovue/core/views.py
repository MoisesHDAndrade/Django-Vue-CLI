from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User

def index(request):
	users = User.objects.all()
	return render(request, 'index.html', {'users':users})

def api_user_request(request):
	users = User.objects.all()
	data = [{'username':user.username} for user in users]
	response = {'data':data}
	return JsonResponse(response)