from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'heading.html')

def women(request):
    return render(request,'women.html')

def men(request):
    return render(request,'men.html')

def kids(request):
    return render(request,'kids.html')

def skincare(request):
    return render(request,'skincare.html')