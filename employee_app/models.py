from django.db import models

class Employee(models.Model):
	employee_id = models.CharField(max_length=100, null=True)
	employee_name = models.CharField(max_length=100, null=True)
	employee_email = models.EmailField()
	employee_contact = models.CharField(max_length=20, null=True)


	def __str__(self):
		return self.employee_name
