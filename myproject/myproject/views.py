from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    #return HttpResponse("Hello, world. You're at homepage.")
    return render(request,'home.html')
def about(request):
  #  return HttpResponse("Hello, world. You're at about page.")
    return render(request,'about.html')

def register(request):
    # Your view logic here
    return render(request, 'register.html')
