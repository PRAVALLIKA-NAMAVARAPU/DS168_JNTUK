from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'login/home.html')

def loggedin(request):
    return render(request,'login/loggedin.html')
