from django.shortcuts import render

def home(request):
	return render(request, 'employee_app/home.html', {})
