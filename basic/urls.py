
from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage , name='home'),

    path('login' , views.loginPage , name='loginPage'),
    path('logout' , views.logoutPage , name='logoutPage'),

  


    path('callback' , views.callBack , name='callBack')
]
