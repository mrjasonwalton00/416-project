from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"), #home url
    path('signUp/', views.signUp, name="signUp"), #sign up url

]

