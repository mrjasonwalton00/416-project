from django.shortcuts import render


# Create your views here.

#home page
def base(request):
    return render(request, 'base/home.html')

#login Page
def login(request):
    return render(request, 'base/login.html')

#Find Professor Page
def findProfessors(request):
    return render(request, 'base/findProfessors.html')

#Profile Page
def profile(request):
    return render(request, 'base/profile.html')

#Test Form
def testForm(request):
    return render(request, 'base/testForm.html')

