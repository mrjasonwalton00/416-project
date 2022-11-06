from django.shortcuts import render


# Create your views here.


#for home page
def home(request):
    return render(request, 'home.html')

#for sign up page
def signUp(request):
    return render(request, 'signUp.html')
