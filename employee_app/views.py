from django.shortcuts import render, redirect
from .forms import EmployeeForm
from . models import Employee
from django.contrib import messages



def home(request):
	return render(request, 'employee_app/home.html', {})
def create_employee(request):
	if request.method == 'POST':
		form = EmployeeForm(request.POST)

		if  form .is_valid():
			form.save()
			return redirect('home')
	else:
		form = EmployeeForm()
	return render(request, 'employee_app/create_employee.html', {
		'form':form
		})

def employee_list(request):
	 employees = Employee.objects.all()
	 return render(request, 'create_employee/list.html', {
	 	'employees':employees
	 	})


def update_employee(request, id):
	employee = Employee.objects.get(pk=id)
	if request.method == 'POST':
		form = EmployeeForm(request.POST, instance=employee)

		if form.is_valid():
			form.save()
			messages.success(request, f'Employee updated successfully')
			return redirect('home')
	else:
		form = EmployeeForm(instance=employee)

	return render(request, 'employee_app/update.html', {
		'form':form
		})
def delete_employee(request, id):
	employee = Employee.objects.get(pk=id)
	if request.method == 'POST':
		employee.delete()
	return redirect('list')