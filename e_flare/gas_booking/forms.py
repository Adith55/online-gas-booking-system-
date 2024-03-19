from django import forms
from .models import Employees

class Employeeform(forms.ModelForm):
    class Meta:
        model= Employees
        fields= ("empCode","fullName","mobileNumber","position")
    