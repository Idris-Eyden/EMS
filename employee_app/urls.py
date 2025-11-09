from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name='home'),
	path('list', views.employee_list, name='list'),
	path('create', views.create_employee, name='create'),
	path('update/<int:id>/', views.update_employee, name='update'),
	path('delete/<int:id>', views.delete_employee, name='delete'),

]