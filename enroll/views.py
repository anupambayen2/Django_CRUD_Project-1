import imp
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import EmployeeRegister
from .models import Employee

# Create your views here.

# This function will add new item or show item.
def add_show(request):
    if request.method == 'POST':
        fm = EmployeeRegister(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            reg = Employee(name=name, email=email, password=password)
            reg.save()
            # fm.save()
            fm = EmployeeRegister()
    else:
        fm = EmployeeRegister()
    emp = Employee.objects.all()
    return render(request, 'enroll/addandshow.html',{'form':fm,'emp':emp})


# This function will update and edit
def update_data(request,id):
    if request.method =='POST':
        pi = Employee.objects.get(pk=id)
        fm = EmployeeRegister(request.POST, instance=pi)
        if fm.is_valid:
            fm.save()
    else:
        pi = Employee.objects.get(pk=id)
        fm = EmployeeRegister(instance=pi)
    return render(request,'enroll/update_employee.html', {'form':fm})

# This function will delete 
def delete_data(request,id):
    if request.method =='POST':
        pi = Employee.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

