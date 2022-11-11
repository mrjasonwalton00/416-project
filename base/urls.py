from django.urls import path
from . import views


urlpatterns = [
    path('', views.base, name="home"), #home url
    path('login/', views.login, name="login"),
    path('findProfessors/', views.findProfessors, name="findProfessors"),
    path('profile/', views.profile, name="profile"),
    path('testForm/', views.testForm, name="testForm"),
    path('jasonHome/', views.jasonHome, name="jasonHome"),
]


