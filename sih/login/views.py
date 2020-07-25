from django.shortcuts import render,redirect
from django.http import HttpResponse
from login.models import *
# Create your views here.
def home(request):
    if request.method=="POST":
        rollno=request.POST['rollno']
        password=request.POST['psw']
        data=student.objects.filter(studentRollno=rollno,password=password)
        if data:
            return render(request,'login/loggedin.html')
        else:
            return redirect('/')
    return render(request,'login/home.html')
def profile(request):
    data=student.objects.get(studentRollno="19021E0027")
    print(data)
    return render(request,'login/profile.html',{'data':data})
def logout(request):
    return redirect('/')
def loggedin(request):
    return render(request,'login/loggedin.html')
