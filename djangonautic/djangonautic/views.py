from django.http import HttpResponse
from django.shortcuts import render

def aboutpage(request):
    #return HttpResponse("This is Django and i am a champion.")
    return render(request,'about.html')
def homepage(request):
    #return HttpResponse("This is the Homepage and follow me.")
    return render(request,'home.html')