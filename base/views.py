from django.shortcuts import render


# Create your views here.

#home page
def base(request):
    return render(request, 'base/home.html')

#login Page
def login(request):
    return render(request, 'base/login.html')

