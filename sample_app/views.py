from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "sample_app/index.html")

def SignUp(request):
    return render(request, "sample_app/SignUp.html")

def SignIn(request):
    return render(request, "sample_app/SignIn.html")

def SignOut(request):
    pass